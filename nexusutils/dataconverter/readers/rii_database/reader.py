#
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
"""Convert refractiveindex.info yaml files to nexus"""
import re
from typing import List, Set, Tuple, Any, Dict
import logging
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import yaml

from nexusutils.dataconverter.readers.json_yml.reader import YamlJsonReader
import nexusutils.dataconverter.readers.rii_database.dispersion_functions as dispersion
from nexusutils.dataconverter.readers.rii_database.formula_parser.parser import (
    transformation_formula_parser,
)
from nexusutils.dataconverter.readers.utils import parse_json


def read_yml_file(filename: str) -> Dict[Any, Any]:
    """Reads a yml file from disk"""
    with open(filename, "r", encoding="utf-8") as yml:
        yml_file = yaml.load(
            yml,
            yaml.SafeLoader,
        )

    return yml_file


def is_table_k_formula_n_disp(dispersion1: dict, dispersion2: dict):
    """Checks if the two dispersions are one tabular k formula and one formula n"""
    if "tabulated k" == dispersion1["type"] and dispersion2["type"].startswith(
        "formula"
    ):
        return True

    if "tabulated k" == dispersion2["type"] and dispersion1["type"].startswith(
        "formula"
    ):
        return True

    return False


def read_metadata(yml_file: dict) -> Dict[str, Any]:
    """Reads metadata from a dispersion yaml file"""
    entries: Dict[str, Any] = {}
    if "REFERENCES" in yml_file:
        pass

    if "COMMENTS" in yml_file:
        pass
    return entries


def write_dispersions(
    yml_file: dict,
    table_input: dispersion.TableInput,
    model_input: dispersion.ModelInput,
):
    """Writes all dispersions from the dict into the entries dict"""

    def write_dispersion(
        dispersion_relation: Dict[str, Any],
        table_input: dispersion.TableInput,
        model_input: dispersion.ModelInput,
    ):
        """Writes a given dispersion relation into the entries dict"""

        type_to_nx_name = {
            "tabulated k": "dispersion_table_k",
            "tabulated n": "dispersion_table_n",
            "tabulated nk": "dispersion_table_nk",
        }
        if dispersion_relation["type"] in dispersion.SUPPORTED_TABULAR_PARSERS:
            table_input.table_type = dispersion_relation["type"]
            table_input.data = dispersion_relation["data"]
            table_input.nx_name = type_to_nx_name[dispersion_relation["type"]]
            dispersion.tabulated(table_input)
            return

        if dispersion_relation["type"] in dispersion.FORMULA_PARSERS:
            coeffs = list(map(float, dispersion_relation["coefficients"].split()))
            model_input.coeffs = coeffs
            dispersion.FORMULA_PARSERS[dispersion_relation["type"]](model_input)
            return

        raise NotImplementedError(f'No parser for type {dispersion_relation["type"]}')

    if len(yml_file["DATA"]) == 2 and is_table_k_formula_n_disp(*yml_file["DATA"]):
        model_input.convert_to_n = True

    for dispersion_relation in yml_file["DATA"]:
        write_dispersion(dispersion_relation, table_input, model_input)


def write_nx_data_to(
    entries: Dict[str, Any],
    path: str,
    wavelength: np.ndarray,
    refractive_index: np.ndarray,
):
    """Writes an NXdata group"""
    entries[f"{path}/@default"] = "plot"
    entries[f"{path}/plot/@axes"] = "wavelength"
    entries[f"{path}/plot/@signal"] = "refractive_index"
    entries[f"{path}/plot/@auxiliary_signals"] = "extinction"
    entries[f"{path}/plot/wavelength"] = wavelength
    entries[f"{path}/plot/wavelength/@units"] = "micrometer"
    entries[f"{path}/plot/refractive_index"] = refractive_index.real
    entries[f"{path}/plot/extinction"] = refractive_index.imag


def write_nx_data(
    entries: Dict[str, Any],
    dispersion_path: str,
    single_params: Dict[str, Dict[str, float]],
    repeated_params: Dict[str, Dict[str, np.ndarray]],
):
    """Calculates and adds dispersions and writes it to a NXdata group."""

    def get_dispersion_names(group_name: str):
        names = set()
        for entry in entries:
            if entry.startswith(f"{dispersion_path}/{group_name}"):
                names.add(re.search(rf"{group_name}\[([^\]]+)\]", entry).group(1))

        return names

    def get_wavelength_index(table_dispersion: str):
        wavelength = entries[
            f"{dispersion_path}/DISPERSION_TABLE[{table_dispersion}]/wavelength"
        ]
        refractive_index = entries[
            f"{dispersion_path}/DISPERSION_TABLE[{table_dispersion}]/refractive_index"
        ]

        return wavelength, refractive_index

    def get_index(wavelength: np.ndarray, func_dispersion: str):
        x_axis_name = entries[
            (
                f"{dispersion_path}/DISPERSION_FUNCTION[{func_dispersion}]"
                "/wavelength_identifier"
            )
        ]
        dfpath = f"{dispersion_path}/DISPERSION_FUNCTION[{func_dispersion}]"
        formula = entries[f"{dfpath}/formula"]

        return transformation_formula_parser(
            x_axis_name,
            wavelength,
            single_params.get(dfpath, {}),
            repeated_params.get(dfpath, {}),
        ).parse(formula)

    def add_func_dispersions(wavelength: np.ndarray, func_dispersions: Set[str]):
        disp_type, refractive_index = get_index(wavelength, func_dispersions.pop())
        for func_dispersion in func_dispersions:
            disp_type2, refractive_index2 = get_index(wavelength, func_dispersion)
            if disp_type2 != disp_type:
                raise ValueError("Incompatible dispersions")
            refractive_index += refractive_index2

        return disp_type, refractive_index

    def add_func_dispersions_entries():
        wavelength = np.linspace(0.4, 1, 500)
        disp_type, refractive_index = add_func_dispersions(wavelength, func_dispersions)

        if disp_type == "eps":
            refractive_index = np.sqrt(refractive_index)

        write_nx_data_to(entries, dispersion_path, wavelength, refractive_index)

    def add_table_func_dispersions_entries():
        wavelength, refractive_index = get_wavelength_index(table_dispersions.pop())
        disp_type, refractive_index_func = add_func_dispersions(
            wavelength, func_dispersions
        )

        if disp_type == "eps":
            raise ValueError(
                "Incompatible dispersions detected: Tabular and eps-based function"
            )

        write_nx_data_to(
            entries,
            dispersion_path,
            wavelength,
            refractive_index + refractive_index_func,
        )

    def add_table_dispersions_entries():
        wlen, rindex = get_wavelength_index(table_dispersions.pop())
        min_wlen = min(wlen)
        max_wlen = max(wlen)
        interpolations = [interp1d(wlen, rindex)]
        for table_dispersion in table_dispersions:
            wlen, rindex = get_wavelength_index(table_dispersion)
            min_wlen = min(wlen) if min(wlen) > min_wlen else min_wlen
            max_wlen = max(wlen) if max(wlen) < max_wlen else max_wlen
            interpolations.append(interp1d(wlen, rindex))

        wavelength = np.linspace(min_wlen, max_wlen, 500)
        refractive_index = np.zeros(wavelength.shape, np.cdouble)
        for interp in interpolations:
            refractive_index += interp(wavelength)

        write_nx_data_to(entries, dispersion_path, wavelength, refractive_index)

    table_dispersions = get_dispersion_names("DISPERSION_TABLE")
    func_dispersions = get_dispersion_names("DISPERSION_FUNCTION")

    if len(table_dispersions) == 1 and func_dispersions:
        add_table_func_dispersions_entries()
        return entries

    if len(table_dispersions) == 0 and func_dispersions:
        add_func_dispersions_entries()
        return entries

    if func_dispersions:
        raise ValueError("Unexpected number of dispersions.")

    if not table_dispersions:
        raise ValueError("No valid dispersions found.")

    add_table_dispersions_entries()
    return entries


def read_dispersion(filename: str, identifier: str = "dispersion_x") -> Dict[str, Any]:
    """Reads a rii dispersion from a yaml file"""
    entries: Dict[str, Any] = {}
    single_params: Dict[str, Dict[str, float]] = {}
    repeated_params: Dict[str, Dict[str, np.ndarray]] = {}

    def add_table(path: str, nx_name: str, daf: pd.DataFrame):
        disp_path = f"{path}/DISPERSION_TABLE[{nx_name}]"

        if f"{disp_path}/refractive_index" in entries:
            if not np.array_equal(entries[f"{disp_path}/wavelength"], daf.index.values):
                raise ValueError(
                    "Trying to add tabular dispersions with different wavelength ranges"
                )
            entries[f"{disp_path}/refractive_index"] += daf["refractive_index"].values
            return

        entries[f"{path}/model_name"] = "Table"
        entries[f"{disp_path}/model_name"] = "Table"
        entries[f"{disp_path}/convention"] = "n + ik"
        entries[f"{disp_path}/wavelength"] = daf.index.values
        entries[f"{disp_path}/wavelength/@units"] = "micrometer"
        entries[f"{disp_path}/refractive_index"] = daf["refractive_index"].values

    def add_model_name(path: str, name: str):
        entries[f"{path}/model_name"] = name

    def add_model_info(
        dispersion_info: dispersion.DispersionInfo,
        model_input: dispersion.ModelInput,
    ):
        disp_path = (
            f"{model_input.dispersion_path}/"
            f"DISPERSION_FUNCTION[{dispersion_info.name.lower()}]"
        )

        entries[f"{disp_path}/model_name"] = dispersion_info.name
        representation = dispersion_info.representation
        formula = dispersion_info.formula
        if dispersion_info.representation == "eps" and model_input.convert_to_n:
            representation = "n"
            formula = f"sqrt({dispersion_info.formula})"
        entries[f"{disp_path}/formula"] = f"{representation} = {formula}"
        entries[f"{disp_path}/representation"] = representation
        entries[f"{disp_path}/convention"] = "n + ik"
        entries[f"{disp_path}/wavelength_identifier"] = "lambda"
        entries[f"{disp_path}/wavelength_identifier/@units"] = "micrometer"

        return disp_path

    def add_single_param(path: str, name: str, value: float, unit: str):
        entries[f"{path}/DISPERSION_SINGLE_PARAMETER[{name}]/name"] = name
        entries[f"{path}/DISPERSION_SINGLE_PARAMETER[{name}]/value"] = value
        entries[f"{path}/DISPERSION_SINGLE_PARAMETER[{name}]/value/@units"] = unit

        single_param_path = single_params.setdefault(path, {})
        single_param_path[name] = value

    def add_rep_param(path: str, name: str, values: List[float], units: List[str]):
        if not units:
            raise ValueError("Units must be specified")

        entries[f"{path}/DISPERSION_REPEATED_PARAMETER[{name}]/name"] = name
        entries[f"{path}/DISPERSION_REPEATED_PARAMETER[{name}]/values"] = values
        if len(units) > 1:
            entries[
                f"{path}/DISPERSION_REPEATED_PARAMETER[{name}]/parameter_units"
            ] = units
        entries[f"{path}/DISPERSION_REPEATED_PARAMETER[{name}]/values/@units"] = units[
            0
        ]

        repeated_param_path = repeated_params.setdefault(path, {})
        repeated_param_path[name] = np.array(values)

    yml_file = read_yml_file(filename)
    dispersion_path = f"/ENTRY[entry]/{identifier}"

    # Only read metadata for the ordinary axis
    # as this should be the same for all axes
    if identifier == "dispersion_x":
        entries.update(read_metadata(yml_file))

    write_dispersions(
        yml_file,
        dispersion.TableInput(dispersion_path, "", "", "", add_table),
        dispersion.ModelInput(
            dispersion_path,
            [],
            False,
            add_model_name,
            add_model_info,
            add_single_param,
            add_rep_param,
        ),
    )

    write_nx_data(entries, dispersion_path, single_params, repeated_params)

    return entries


def fill_dispersion_in(template: Dict[str, Any]):
    """
    Replaces dispersion_x and dispersion_y keys with filenames as their value
    with the parsed dispersion values.
    """
    keys = [f"dispersion_{axis}" for axis in ["y", "z"]]

    for key in keys:
        if key in template:
            template.update(read_dispersion(template[key], identifier=key))
            del template[key]


def parse_json_w_fileinfo(filename: str) -> Dict[str, Any]:
    """
    Reads json key/value pairs and additionally replaces dispersion_x and _y keys
    with their parsed dispersion values.
    """
    template = parse_json(filename)
    fill_dispersion_in(template)

    return template


def handle_objects(objects: Tuple[Any]) -> Dict[str, Any]:
    """Handle objects and generate template entries from them"""
    if objects is None:
        return {}

    template = {}

    for obj in objects:
        if not isinstance(obj, dict):
            logging.warning("Ignoring unknown object of type %s", type(obj))
            continue

        template.update(obj)

    fill_dispersion_in(template)

    return template


def appdef_defaults() -> Dict[str, Any]:
    """Fills default entries which are comment for the application
    definition. Like appdef version and name"""
    entries: Dict[str, Any] = {}

    entries["/ENTRY[entry]/definition/@version"] = "0.0.1"
    entries["/ENTRY[entry]/definition/@url"] = ""
    entries["/ENTRY[entry]/definition"] = "NXdispersive_material"

    entries["/@default"] = "entry"
    entries["/ENTRY[entry]/@default"] = "dispersion_x"

    return entries


# pylint: disable=too-few-public-methods
class RiiReader(YamlJsonReader):
    """
    Converts refractiveindex.info yaml files to nexus
    """

    supported_nxdls = ["NXdispersive_material"]
    extensions = {
        ".yml": read_dispersion,
        ".yaml": read_dispersion,
        ".json": parse_json_w_fileinfo,
        "default": lambda _: appdef_defaults(),
        "objects": handle_objects,
    }


READER = RiiReader
