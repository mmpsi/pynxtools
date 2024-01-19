"""
A generic reader for loading XPS (X-ray Photoelectron Spectroscopy) data
file into mpes nxdl (NeXus Definition Language) template.
"""
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from pathlib import Path
from typing import Any, Dict, Set, List, Tuple
import sys
import json
import datetime

import yaml
import numpy as np

from pynxtools.dataconverter.readers.base.reader import BaseReader
from pynxtools.dataconverter.readers.utils import (
    FlattenSettings,
    flatten_and_replace,
    parse_flatten_json,
)
from pynxtools.dataconverter.template import Template
from pynxtools.dataconverter.helpers import extract_atom_types

from pynxtools.dataconverter.readers.xps.file_parser import XpsDataFileParser
from pynxtools.dataconverter.readers.xps.reader_utils import construct_entry_name

np.set_printoptions(threshold=sys.maxsize)

XPS_TOKEN = "@xps_token:"
XPS_DATA_TOKEN = "@data:"
XPS_DETECTOR_TOKEN = "@detector_data:"
ELN_TOKEN = "@eln"
LINK_TOKEN = "link"
TOKEN_SET = {XPS_TOKEN, XPS_DATA_TOKEN, XPS_DETECTOR_TOKEN, ELN_TOKEN}

# Track entries for using for eln data
ENTRY_SET: Set[str] = set()
DETECTOR_SET: Set[str] = set()
POSSIBLE_ENTRY_PATH: Dict = {}


CONVERT_DICT = {
    "unit": "@units",
    "version": "@version",
    "user": "USER[user]",
    "instrument": "INSTRUMENT[instrument]",
    "source_probe": "SOURCE[source_probe]",
    "beam_probe": "BEAM[beam_probe]",
    "analyser": "ELECTRONANALYSER[electronanalyser]",
    "collectioncolumn": "COLLECTIONCOLUMN[collectioncolumn]",
    "energydispersion": "ENERGYDISPERSION[energydispersion]",
    "detector": "DETECTOR[detector]",
    "manipulator": "MANIPULATOR[manipulator]",
    "pid": "PID[pid]",
    "process": "PROCESS[process]",
    "sample": "SAMPLE[sample]",
    "substance": "SUBSTANCE[substance]",
    # "Data": "DATA[data]",
}

REPLACE_NESTED: Dict[str, str] = {}


def find_entry_and_value(xps_data_dict, key_part, dt_typ):
    """Construct the entry name and pick up the corresponding data for
    that for that entry.
    """

    entries_values = {}
    if dt_typ == XPS_TOKEN:
        for key, val in xps_data_dict.items():
            if key.endswith(key_part):
                entry = construct_entry_name(key)
                entries_values[entry] = val

    elif dt_typ in (XPS_DATA_TOKEN, XPS_DETECTOR_TOKEN):
        # entries_values = entry:{cycle0_scan0_chan0:xr.data}
        entries_values = xps_data_dict["data"]

    return entries_values


def get_entries_and_detectors(config_dict, xps_data_dict):
    """Get all entries in the xps_data_dict"""
    for key, value in config_dict.items():
        for token in [XPS_DATA_TOKEN, XPS_DETECTOR_TOKEN, XPS_TOKEN]:
            try:
                key_part = value.split(token)[-1]
                entries_values = find_entry_and_value(
                    xps_data_dict, key_part, dt_typ=token
                )

                for entry, data in entries_values.items():
                    if entry:
                        ENTRY_SET.add(entry)
                    if token == XPS_DETECTOR_TOKEN:
                        chan_count = "_chan"
                        # Iteration over scan
                        for data_var in data.data_vars:
                            if chan_count in data_var:
                                detector_num = data_var.split("_chan_")[-1]
                                detector_nm = f"detector{detector_num}"
                                DETECTOR_SET.add(detector_nm)
            except AttributeError:
                continue


# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
def fill_data_group(key, entries_values, config_dict, template):
    """Fill out fields and attributes for NXdata"""

    survey_count_ = 0
    count = 0

    for entry, xr_data in entries_values.items():
        modified_key = key.replace("entry", entry)
        modified_key = modified_key.replace("[data]/data", "[data]")
        root = key[0]
        modified_entry = key[0:13]
        modified_entry = modified_entry.replace("entry", entry)

        template[f"{modified_entry}/@default"] = "data"

        # Set first Survey as default for .nxs file
        if "Survey" in entry and survey_count_ == 0:
            survey_count_ = survey_count_ + 1
            template[f"{root}@default"] = entry

        # If no Survey set any scan for default
        if survey_count_ == 0 and count == 0:
            count = count + 1
            template[f"{root}@default"] = entry

        binding_energy_coord = None
        chan_count = "_chan"
        for data_var in xr_data.data_vars:
            scan = data_var
            # Collecting only accumulated counts
            # indivisual channeltron counts goes to detector data section
            if chan_count not in scan:
                key_indv_scn_dt = f"{modified_key}/{scan}"

                key_indv_scn_dt_unit = f"{key_indv_scn_dt}/@units"

                coord_nm = list(xr_data[data_var].coords)[0]
                binding_energy_coord = np.array(xr_data[data_var][coord_nm])
                template[key_indv_scn_dt] = xr_data[data_var].data
                template[key_indv_scn_dt_unit] = config_dict[f"{key}/@units"]

        data_key = f"{modified_key}/data"
        data_unit_key = f"{data_key}/@units"
        data_default_key = f"{modified_key}/@default"
        data_signal_key = f"{modified_key}/@signal"
        data_axis_key = f"{modified_key}/@axes"

        energy_key = f"{modified_key}/energy"
        energy_unit_key = f"{energy_key}/@units"
        energy_indices_key = f"{modified_key}/@energy_indices"
        energy_indices_key = f"{modified_key}/@energy_depends"

        template[data_signal_key] = "data"

        template[data_key] = np.mean(
            [
                xr_data[x_arr].data
                for x_arr in xr_data.data_vars
                if "_chan" not in x_arr
            ],
            axis=0,
        )

        template[f"{data_key}_errors"] = np.std(
            [
                xr_data[x_arr].data
                for x_arr in xr_data.data_vars
                if "_chan" not in x_arr
            ],
            axis=0,
        )

        template[data_unit_key] = config_dict[f"{key}/@units"]
        template[key_be_unit] = "eV"
        template[key_be] = binding_energy_coord
        template[key_be_axes] = energy_name
        template[key_be_ind] = energy_index
        template[key_nxclass] = "NXdata"
        template[key_ax_ln_nm] = long_name
        template[key_ax_mn] = energy_index

        # =============================================================================
        #         "data":{
        #   "@signal":"",
        #   "@default":"data",
        #   "data":"@data:cycle",
        #   "data/@units":"@xps_token:data/intensity/@units",
        #   "energy":"@data:energy",
        #   "energy/@type":"@xps_token:data/energy_type",
        #   "energy/@units":"@xps_token:data/energy/@units",
        #   "/@energy_indices":"None",
        #   "@energy_depends":"None"
        #
        #
        #
        #
        #
        #         "data":{
        #             "@signal":"",
        #             "@":"data",
        #             "data":"@data:cycle",
        #             "data/@units":"@xps_token:data/intensity/@units",
        #             "energy":"@data:energy",
        #             "energy/@type":"@xps_token:data/energy_type",
        #             "energy/@units":"@xps_token:data/energy/@units",
        #             "/@":"None",
        #             "@energy_depends":"None"
        #
        #
        # =============================================================================
        energy_name = "energy"
        energy_index = 0
        key_be = f"{modified_key}/{energy_name}"
        key_be_unit = f"{key_be}/@units"
        key_be_axes = f"{modified_key}/@axes"
        key_be_ind = f"{modified_key}/@{energy_name}_indices"

        # setting up AXISNAME
        axisname = "AXISNAME[axisname]"
        long_name = "Binding Energy"
        key_ax_mn = f"{modified_key}/{axisname}"
        key_ax_ln_nm = f"{modified_key}/{axisname}/@long_name"

        key_nxclass = f"{modified_key}/@NX_class"


def fill_detector_group(key, entries_values, config_dict, template):
    """Fill out fileds and attributes for NXdetector/NXdata"""

    for entry, xr_data in entries_values.items():
        cycle_count = "cycle"
        scan_count = "_scan"
        chan_count = "_chan"

        # Iteration over scan
        for data_var in xr_data.data_vars:
            if chan_count in data_var:
                detector_num = data_var.split("_chan_")[-1]
                detector_nm = f"detector{detector_num}"
                cycle_scan_num = data_var.split(chan_count)[0]
                print(cycle_scan_num)
                scan_num = 0
                # (scan_count)[-1].split(chan_count)[0]
                scan_nm = f"scan_{scan_num}"
                modified_key = key.replace("entry", entry)
                modified_key = modified_key.replace("[detector]", f"[{detector_nm}]")
                modified_key_unit = modified_key + "/@units"
                scan_key = modified_key.replace("raw_data/raw", f"raw_data/{scan_nm}")

                template[scan_key] = xr_data[data_var].data


def fill_template_with_value(key, value, template):
    """
    Fill NeXus template with a key-value pair.

    Parameters
    ----------
    key : str
        DESCRIPTION.
    value :
        Any value coming from the XPS, config, or ELN file.
    template : Template
        A NeXus template.

    """
    if value is None or str(value) == "None":
        return

    # Do for all entry names
    for entry in ENTRY_SET:
        atom_types: List = []
        if "chemical_formula" in key:
            atom_types = list(extract_atom_types(value))

        if isinstance(value, datetime.datetime):
            value = value.isoformat()

        elif isinstance(value, dict) and LINK_TOKEN in value:
            link_text = value[LINK_TOKEN]
            link_text = link_text.replace("entry", f"{entry}")
            value = {LINK_TOKEN: link_text}

        modified_key = key.replace("[entry]", f"[{entry}]")

        # Do for all detectors
        if "[detector]" in key:
            for detector in DETECTOR_SET:
                detr_key = modified_key.replace("[detector]", f"[{detector}]")
                template[detr_key] = value

                if isinstance(value, dict) and LINK_TOKEN in value:
                    link_text = value[LINK_TOKEN]
                    if "/detector/" in link_text:
                        # Only replace if generic detector is given in
                        # link.
                        link_text = link_text.replace("detector", f"{detector}")
                        value = {LINK_TOKEN: link_text}

                template[detr_key] = value
        else:
            template[modified_key] = value

        if atom_types:
            modified_key = modified_key.replace("chemical_formula", "atom_types")
            template[modified_key] = ", ".join(atom_types)


def fill_template_with_xps_data(config_dict, xps_data_dict, template):
    """Collect the xps data from xps_data_dict
    and store them into template. We use searching_keys
    for separating the data from xps_data_dict.
    """
    for key, config_value in config_dict.items():
        if isinstance(config_value, str) and any(
            token in config_value for token in TOKEN_SET
        ):
            # ===========================================================================
            #             if XPS_DATA_TOKEN in str(config_value):
            #                 key_part = config_value.split(XPS_DATA_TOKEN)[-1]
            #                 entries_values = find_entry_and_value(
            #                     xps_data_dict, key_part, dt_typ=XPS_DATA_TOKEN
            #                 )
            #
            #                 fill_data_group(key, entries_values, config_dict, template)
            # ===========================================================================

            if XPS_DETECTOR_TOKEN in str(config_value):
                key_part = config_value.split(XPS_DATA_TOKEN)[-1]
                entries_values = find_entry_and_value(
                    xps_data_dict, key_part, dt_typ=XPS_DETECTOR_TOKEN
                )

                fill_detector_group(key, entries_values, config_dict, template)

            elif XPS_TOKEN in str(config_value):
                token = config_value.split(XPS_TOKEN)[-1]
                entries_values = find_entry_and_value(
                    xps_data_dict, token, dt_typ=XPS_TOKEN
                )
                for entry, ent_value in entries_values.items():
                    fill_template_with_value(key, ent_value, template)  #

        else:
            # Fill with config value.
            fill_template_with_value(key, config_value, template)


def fill_template_with_eln_data(eln_data_dict, config_dict, template):
    """Fill the template from provided eln data"""
    for key, config_value in config_dict.items():
        if ELN_TOKEN in str(config_value):
            field_value = eln_data_dict[key]
            fill_template_with_value(key, field_value, template)
        elif key in eln_data_dict:
            field_value = eln_data_dict[key]
            fill_template_with_value(key, field_value, template)


def concatenate_values(value1, value2):
    """
    Concatenate two values of same type to be stored
    in xps_data_dict. Dicts are merged and every other object is
    appended to a list.

    """
    if isinstance(value1, dict) and isinstance(value2, dict):
        concatenated = {**value1, **value2}
    else:
        if not isinstance(value1, list):
            value1 = [value1]
        if not isinstance(value2, list):
            value2 = [value2]
        concatenated = value1 + value2

    return concatenated


# pylint: disable=too-few-public-methods
class XPSReader(BaseReader):
    """Reader for XPS."""

    supported_nxdls = [
        "NXmpes",
    ]

    def read(
        self,
        template: dict = None,
        file_paths: Tuple[str] = None,
        objects: Tuple[Any] = None,
        **kwargs,
    ) -> dict:
        """Reads data from given file and returns
        a filled template dictionary"""

        reader_dir = Path(__file__).parent

        xps_data_dict: Dict[str, Any] = {}
        eln_data_dict: Dict[str, Any] = {}
        config_file: Path = reader_dir.joinpath("config", "template.json")

        for file in file_paths:
            file_ext = file.rsplit(".")[-1]

            if file_ext in ["yaml", "yml"]:
                with open(file, mode="r", encoding="utf-8") as eln:
                    eln_data_dict = flatten_and_replace(
                        FlattenSettings(
                            yaml.safe_load(eln), CONVERT_DICT, REPLACE_NESTED
                        )
                    )
            elif file_ext in XpsDataFileParser.__prmt_file_ext__:
                parser = XpsDataFileParser([file])
                data_dict = parser.get_dict(**kwargs)
                config_file = parser.config_file

                # If there are multiple input data files of the same type,
                # make sure that existing keys are not overwritten.
                existing = [
                    (key, xps_data_dict[key], data_dict[key])
                    for key in set(xps_data_dict).intersection(data_dict)
                ]

                xps_data_dict = {**xps_data_dict, **data_dict}
                for key, value1, value2 in existing:
                    xps_data_dict[key] = concatenate_values(value1, value2)

                config_file = reader_dir.joinpath(f"config/{config_file}")
            elif file_ext in XpsDataFileParser.__prmt_metadata_file_ext__:
                data_dict = XpsDataFileParser([file]).get_dict(**kwargs)

                xps_data_dict = {**xps_data_dict, **data_dict}

            # This code is not very robust.
            elif file_ext == "json":
                if "config" in file:
                    config_file = file

        config_dict = parse_flatten_json(config_file)

        get_entries_and_detectors(config_dict, xps_data_dict)
        fill_template_with_xps_data(config_dict, xps_data_dict, template)

        if eln_data_dict:
            # Filling in ELN metadata and overwriting the common
            # paths by giving preference to the ELN metadata
            fill_template_with_eln_data(eln_data_dict, config_dict, template)
        else:
            raise ValueError(
                "Eln file must be submited with some required fields and attributes."
            )

        final_template = Template()
        for key, val in template.items():
            if ("/ENTRY[entry]" not in key) and (val is not None):
                final_template[key] = val

        return final_template


READER = XPSReader
