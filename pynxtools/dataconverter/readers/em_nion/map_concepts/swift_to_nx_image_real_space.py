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
"""The constraints defining if a swift display_item is assumed a NxImageRealSpace concept."""

# pylint: disable=no-member,line-too-long

# releasing line-too-long restriction to avoid having line breaks in the mapping table
# made the experience that when having a widescreen working with the mapping table
# as single-line instructions is more convenient to read and parsable by human eye

# current issues:
# hard-coding currently the ebeam deflector is problematic as it is
# to just make the name variadic but then assume there is always only one
# in the specific case of a Nion microscope and which information is available typically
# via swift there one would get information about the scanbox for which the closest
# match is NXebeam_deflector and there is only one scanbox at an Nion Hermes 200
# but one could customize this implementation here and instead resolve how the scanbox
# is composed of individual groups of deflection coils in which case one could also
# think about using one NXebeam_deflector for every single coil...

NxImageRealSpaceDict = {
    "IGNORE": {"fun": "load_from", "terms": "type"},
    "IGNORE": {"fun": "load_from", "terms": "uuid"},
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/start_time": {
        "fun": "convert_iso8601",
        "terms": ["created", "timezone"],
    },
    "IGNORE": {"fun": "load_from", "terms": "is_sequence"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/offset"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/scale"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/units"},
    "IGNORE": {"fun": "load_from", "terms": "dimensional_calibrations"},
    "IGNORE": {"fun": "load_from", "terms": "timezone"},
    "IGNORE": {"fun": "load_from", "terms": "timezone_offset"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/high_tension"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/defocus"},
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/electron_source/voltage": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/EHT",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/electron_source/voltage/@units": "V",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/PMTBF_gain",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/PMTDF_gain",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/tilt1": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutA",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/tilt1/@units": "deg",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/tilt2": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutB",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/tilt2/@units": "deg",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/position": {
        "fun": "load_from",
        "terms": [
            "metadata/instrument/ImageScanned/StageOutX",
            "metadata/instrument/ImageScanned/StageOutY",
            "metadata/instrument/ImageScanned/StageOutZ",
        ],
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/STAGE_LAB[stage_lab]/position/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_0/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C10",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_0/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_2_a/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C12.a",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_2_a/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_2_b/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C12.b",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_1_2_b/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_1_a/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C21.a",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_1_a/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_1_b/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C21.b",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_1_b/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_3_a/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C23.a",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_3_a/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_3_b/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C23.b",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_2_3_b/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_0/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C30",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_0/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_2_a/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C32.a",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_2_a/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_2_b/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C32.b",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_2_b/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_4_a/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C34.a",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_4_a/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_4_b/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C34.b",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_3_4_b/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_5_0/magnitude": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C50",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/aberration_correction/ZEMLIN_TABLEAU/PROCESS[process]/nion/c_5_0/magnitude/@units": "m",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em1]/value": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C1 ConstW",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em1]/name": "C1",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em2]/value": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C2 ConstW",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em2]/name": "C2",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em3]/value": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C3 ConstW",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_COLUMN[ebeam_column]/LENS_EM[lens_em3]/name": "C3",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/PMT2_gain",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/SuperFEG.^EmissionCurrent",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/G_2Db"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/LastTuneCurrent",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/OPTICAL_SYSTEM_EM[optical_system_em]/semi_convergence_angle": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/probe_ha",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/OPTICAL_SYSTEM_EM[optical_system_em]/semi_convergence_angle/@units": "mrad",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/IMAGE_SET[image_set*]/inner_half_angle": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/HAADF_Inner_ha",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/IMAGE_SET[image_set*]/inner_half_angle/@units": "mrad",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/IMAGE_SET[image_set*]/outer_half_angle": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/HAADF_Outer_ha",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/IMAGE_SET[image_set*]/outer_half_angle/@units": "mrad",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/GeometricProbeSize",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/hardware_source_id"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/hardware_source_name"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_id"},
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/center": {
        "fun": "load_from",
        "terms": ["metadata/scan/center_x_nm", "metadata/scan/center_y_nm"],
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/center/@units": "nm",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/OPTICAL_SYSTEM_EM[optical_system_em]/field_of_view": {
        "fun": "load_from",
        "terms": "metadata/scan/fov_nm",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/OPTICAL_SYSTEM_EM[optical_system_em]/field_of_view/@units": "nm",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/rotation": {
        "fun": "load_from",
        "terms": "metadata/scan/rotation",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/rotation/@units": "deg",
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/rotation_deg"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_context_size"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/scan/subscan_fractional_size"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_size"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/scan/subscan_fractional_center"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/size",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/center_nm",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/pixel_time_us",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/fov_nm",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/rotation_rad",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/external_clock_wait_time": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_clock_wait_time_ms",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/external_clock_wait_time": "ms",
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/external_clock_mode": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_clock_mode",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/external_scan_mode": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_scan_mode",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/external_scan_ratio": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_scan_ratio",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/ac_line_sync",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/ac_frame_sync": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/ac_frame_sync",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/flyback_time_us",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/subscan_pixel_size",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/subscan_fractional_size",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/subscan_fractional_center",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/top_left_override",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/data_shape_override",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/state_override",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/section_rect",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/scan_id",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/ac_line_sync": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/ac_line_sync",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/calibration_style": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/calibration_style",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/center_x_nm",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/center_y_nm",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/flyback_time": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/flyback_time_us",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/flyback_time/@units": "µs",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/fov_nm",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/line_time": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/line_time_us",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/line_time/@units": "µs",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/pixel_time_us",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/pixels_x",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/pixels_y",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/pixel_time_target": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/requested_pixel_time_us",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/pixel_time_target/@units": "µs",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/rotation_deg",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/rotation_rad",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac1]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 0",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac2]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 1",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac3]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 2",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac4]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 3",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac5]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 4",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac6]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 5",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac7]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 6",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac8]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 7",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac9]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 8",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac10]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 9",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac11]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 10",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/DAC[dac12]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 DAC 11",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board1]/relay": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 0 Relay",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac1]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 0",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac2]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 1",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac3]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 2",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac4]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 3",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac5]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 4",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac6]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 5",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac7]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 6",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac8]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 7",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac9]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 8",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac10]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 9",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac11]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 10",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/DAC[dac12]/value": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 DAC 11",
    },
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/em_lab/EBEAM_DEFLECTOR[ebeam_deflector1]/CIRCUIT_BOARD[mag_board2]/relay": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_properties/mag_boards/MagBoard 1 Relay",
    },
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/scan/valid_rows"},
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/IMAGE_SET[image_set*]/detector_identifier": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/hardware_source_id",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/hardware_source_name",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/exposure"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/hardware_source/frame_index"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/channel_id"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/channel_name"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/pixel_time_us"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/line_time_us"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/hardware_source/valid_rows"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/hardware_source/channel_index"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/hardware_source/reference_key"},
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/hardware_source/view_id"},
    "IGNORE": {"fun": "load_from", "terms": "title"},
    "IGNORE": {"fun": "load_from", "terms": "session_id"},
    "IGNORE": {"fun": "load_from", "terms": "session"},
    "IGNORE": {"fun": "load_from", "terms": "category"},
    "IGNORE": {"fun": "load_from", "terms": "version"},
    "IGNORE": {"fun": "load_from", "terms": "modified"},
    "IGNORE": {"fun": "load_from", "terms": "data_shape"},
    "IGNORE": {"fun": "load_from", "terms": "data_dtype"},
    "IGNORE": {"fun": "load_from", "terms": "collection_dimension_count"},
    "IGNORE": {"fun": "load_from", "terms": "datum_dimension_count"},
    "/ENTRY[entry*]/measurement/EVENT_DATA_EM[event_data_em*]/end_time": {
        "fun": "convert_iso8601",
        "terms": ["data_modified", "timezone"],
    },
}
