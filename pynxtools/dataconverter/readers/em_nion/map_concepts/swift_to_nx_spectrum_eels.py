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
"""The constraints defining if a swift display_item is assumed a NxSpectrumSetEels concept."""

# pylint: disable=no-member,line-too-long

# releasing line-too-long restriction to avoid having line breaks in the mapping table
# made the experience that when having a widescreen working with the mapping table
# as single-line instructions is more convenient to read and parsable by human eye


NxSpectrumEels = {
    "IGNORE": {"fun": "load_from", "terms": "type"},
    "IGNORE": {"fun": "load_from", "terms": "uuid"},
    "IGNORE": {"fun": "convert_iso8601", "terms": ["created", "timezone"]},
    "IGNORE": {"fun": "load_from", "terms": "is_sequence"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/offset"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/scale"},
    "IGNORE": {"fun": "load_from", "terms": "intensity_calibration/units"},
    "IGNORE": {"fun": "load_from", "terms": "dimensional_calibrations"},
    "IGNORE": {"fun": "load_from", "terms": "timezone_offset"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/header_info/header_detail",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/header_info/htype",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/header_info/series",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/auto_summation",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/beam_center_x",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/beam_center_y",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/bit_depth_image",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/bit_depth_readout",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/chi_increment",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/chi_start",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/compression",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/count_time",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/countrate_correction_applied",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/countrate_correction_count_cutoff",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/data_collection_date",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/description",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/detector_distance",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/detector_number",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/detector_readout_time",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/detector_translation",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/eiger_fw_version",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/element",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/flatfield_correction_applied",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/frame_count_time",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/frame_period",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/frame_time",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/kappa_increment",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/kappa_start",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/nimages",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/ntrigger",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/number_of_excluded_pixels",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/omega_increment",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/omega_start",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/phi_increment",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/phi_start",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/photon_energy",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/pixel_mask_applied",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/roi_mode",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/sensor_material",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/sensor_thickness",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/software_version",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/threshold_energy",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/trigger_mode",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/two_theta_increment",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/two_theta_start",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/virtual_pixel_correction_applied",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/wavelength",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/x_pixel_size",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/x_pixels_in_detector",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/y_pixel_size",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/detector_configuration/y_pixels_in_detector",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/bad_pixels",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/processing",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/flip_l_r",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/binning",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/chip_size",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/sensor_dimensions",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/readout_area",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/countrate_correction_cutoff",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/interpolate_racetracks",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/mark_saturated_pixels",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/apply_countrate_correction",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/countrate_correction_factor",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/apply_gain_correction",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/camera_processing_parameters/always_interpolate_racetracks",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/high_tension"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/defocus"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/EHT",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/MajorOL",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/StageOutA",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/StageOutB",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/StageOutX",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/StageOutY",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/StageOutZ",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/probe_ha",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/SuperFEG.^EmissionCurrent",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/LastTuneCurrent",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C10",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C12.a",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C12.b",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C21.a",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C21.b",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C23.a",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C23.b",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C30",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C32.a",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C32.b",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C34.a",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C34.b",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/ImageRonchigram/C50",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/hardware_source_id",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/hardware_source/hardware_source_name",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/exposure"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/binning"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/hardware_source/signal_type"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/hardware_source_id"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/hardware_source_name"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_id"},
    "IGNORE": {
        "fun": "load_from",
        "terms": ["metadata/scan/center_x_nm", "metadata/scan/center_y_nm"],
    },
    "IGNORE": "nm",
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/fov_nm"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/rotation"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/rotation_deg"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_context_size"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/scan_size"},
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
    "IGNORE": "µs",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/fov_nm",
    },
    "IGNORE": "nm",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/rotation_rad",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_clock_wait_time_ms",
    },
    "IGNORE": "ms",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_clock_mode",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_scan_mode",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/external_scan_ratio",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/ac_line_sync",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/ac_frame_sync",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/flyback_time_us",
    },
    "IGNORE": "µs",
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/scan/scan_device_parameters/scan_id",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/scan/valid_rows"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/high_tension"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/defocus"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/EHT"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/PMTBF_gain",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/PMTDF_gain",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutA",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutB",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutX",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutY",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/StageOutZ",
    },
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C10"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C12.a"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C12.b"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C21.a"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C21.b"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C23.a"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C23.b"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C30"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C32.a"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C32.b"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C34.a"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C34.b"},
    "IGNORE": {"fun": "load_from", "terms": "metadata/instrument/ImageScanned/C50"},
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C1 ConstW",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C2 ConstW",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/C3 ConstW",
    },
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
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/probe_ha",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/HAADF_Inner_ha",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/HAADF_Outer_ha",
    },
    "IGNORE": {
        "fun": "load_from",
        "terms": "metadata/instrument/ImageScanned/GeometricProbeSize",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/x_shifter",
    },
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/MultiAcquire.settings/blanker"},
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/x_shift_delay",
    },
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/MultiAcquire.settings/focus"},
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/focus_delay",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/auto_dark_subtract",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/processing",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/blanker_delay",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/sum_frames",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/camera_hardware_source_id",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/use_multi_eels_calibration",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/shift_each_sequence_slice",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/y_shifter",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/x_units_per_ev",
    },
    "UNCLEAR": "eV",
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/y_units_per_px",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/y_shift_delay",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/saturation_value",
    },
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/MultiAcquire.settings/y_align"},
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.settings/stitch_spectra",
    },
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/MultiAcquire.parameters/index"},
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.parameters/offset_x",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.parameters/offset_y",
    },
    "UNCLEAR": {
        "fun": "load_from",
        "terms": "metadata/MultiAcquire.parameters/exposure_ms",
    },
    "UNCLEAR": "ms",
    "UNCLEAR": {"fun": "load_from", "terms": "metadata/MultiAcquire.parameters/frames"},
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
    "IGNORE": {"fun": "convert_iso8601", "terms": ["data_modified", "timezone"]},
    "UNCLEAR": {"fun": "load_from", "terms": "session/site"},
}

# {"fun": "convert_iso8601", "terms": ["created", "timezone"]}
