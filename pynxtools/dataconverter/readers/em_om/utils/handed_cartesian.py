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
"""Definitions for right- or left-handed Cartesian coordinate system."""

# pylint: disable=no-member

# the nxebsd.schema.archive.yaml" offers a set of sets of RadioEditButtons
# each such set can be used to define the unique orientation of a right-handed
# Cartesian coordinate system's base vectors when viewed by an outer observer
# looking to the display of the coordinate system triplet vector and comparing
# to the plane of sight and a compass
# the compass defines four directions, north aka up, east aka right, south aka down,
# and west aka left. The plane of sight defines two additional directions in aka
# into the plane and out aka out-of-the-plane
# there are different strategies what users find convenient to report to specify
# the directions into which the base vectors are assumed pointing
# in general only two perpendicular directions have to be specified as the third
# follows implicitly i.e. there is no need to overconstraint hence the term "undefined"
# the following dictionary is a lookup table whereby the input of the user
# can be evaluated to check if the radioeditbutton choice result in a fully constraint
# and thus unique definition. All other choices are reported as a not fully constraint
# i.e. eventually problematic coordinate system

REFERENCE_FRAMES = ["undefined", "right_handed_cartesian", "left_handed_cartesian"]

AXIS_DIRECTIONS = ["undefined", "north", "east", "south", "west", "in", "out"]

# is a right-handed Cartesian coordinate system sufficiently constrained, when
# at least two base vector directions are chosen
is_cs_rh_unambiguous = {
    "undefined_undefined_undefined": False,
    "undefined_undefined_north": False,
    "undefined_undefined_east": False,
    "undefined_undefined_south": False,
    "undefined_undefined_west": False,
    "undefined_undefined_in": False,
    "undefined_undefined_out": False,
    "undefined_north_undefined": False,
    "undefined_north_north": False,
    "undefined_north_east": True,
    "undefined_north_south": True,
    "undefined_north_west": True,
    "undefined_north_in": True,
    "undefined_north_out": True,
    "undefined_east_undefined": False,
    "undefined_east_north": True,
    "undefined_east_east": False,
    "undefined_east_south": True,
    "undefined_east_west": False,
    "undefined_east_in": True,
    "undefined_east_out": True,
    "undefined_south_undefined": False,
    "undefined_south_north": False,
    "undefined_south_east": True,
    "undefined_south_south": False,
    "undefined_south_west": True,
    "undefined_south_in": True,
    "undefined_south_out": True,
    "undefined_west_undefined": False,
    "undefined_west_north": True,
    "undefined_west_east": False,
    "undefined_west_south": True,
    "undefined_west_west": False,
    "undefined_west_in": True,
    "undefined_west_out": True,
    "undefined_in_undefined": False,
    "undefined_in_north": True,
    "undefined_in_east": True,
    "undefined_in_south": True,
    "undefined_in_west": True,
    "undefined_in_in": False,
    "undefined_in_out": False,
    "undefined_out_undefined": False,
    "undefined_out_north": True,
    "undefined_out_east": True,
    "undefined_out_south": True,
    "undefined_out_west": True,
    "undefined_out_in": False,
    "undefined_out_out": False,
    "north_undefined_undefined": False,
    "north_undefined_north": False,
    "north_undefined_east": True,
    "north_undefined_south": False,
    "north_undefined_west": True,
    "north_undefined_in": True,
    "north_undefined_out": True,
    "north_north_undefined": False,
    "north_north_north": False,
    "north_north_east": False,
    "north_north_south": False,
    "north_north_west": False,
    "north_north_in": False,
    "north_north_out": False,
    "north_east_undefined": True,
    "north_east_north": False,
    "north_east_east": False,
    "north_east_south": False,
    "north_east_west": False,
    "north_east_in": True,
    "north_east_out": False,
    "north_south_undefined": False,
    "north_south_north": False,
    "north_south_east": False,
    "north_south_south": False,
    "north_south_west": False,
    "north_south_in": False,
    "north_south_out": False,
    "north_west_undefined": True,
    "north_west_north": False,
    "north_west_east": False,
    "north_west_south": False,
    "north_west_west": False,
    "north_west_in": False,
    "north_west_out": True,
    "north_in_undefined": True,
    "north_in_north": False,
    "north_in_east": False,
    "north_in_south": False,
    "north_in_west": True,
    "north_in_in": False,
    "north_in_out": False,
    "north_out_undefined": True,
    "north_out_north": False,
    "north_out_east": True,
    "north_out_south": False,
    "north_out_west": False,
    "north_out_in": False,
    "north_out_out": False,
    "east_undefined_undefined": False,
    "east_undefined_north": True,
    "east_undefined_east": False,
    "east_undefined_south": True,
    "east_undefined_west": False,
    "east_undefined_in": True,
    "east_undefined_out": True,
    "east_north_undefined": True,
    "east_north_north": False,
    "east_north_east": False,
    "east_north_south": False,
    "east_north_west": False,
    "east_north_in": False,
    "east_north_out": True,
    "east_east_undefined": False,
    "east_east_north": False,
    "east_east_east": False,
    "east_east_south": False,
    "east_east_west": False,
    "east_east_in": False,
    "east_east_out": False,
    "east_south_undefined": True,
    "east_south_north": False,
    "east_south_east": False,
    "east_south_south": False,
    "east_south_west": False,
    "east_south_in": True,
    "east_south_out": False,
    "east_west_undefined": False,
    "east_west_north": False,
    "east_west_east": False,
    "east_west_south": False,
    "east_west_west": False,
    "east_west_in": False,
    "east_west_out": False,
    "east_in_undefined": True,
    "east_in_north": True,
    "east_in_east": False,
    "east_in_south": False,
    "east_in_west": False,
    "east_in_in": False,
    "east_in_out": False,
    "east_out_undefined": True,
    "east_out_north": False,
    "east_out_east": False,
    "east_out_south": True,
    "east_out_west": False,
    "east_out_in": False,
    "east_out_out": False,
    "south_undefined_undefined": False,
    "south_undefined_north": False,
    "south_undefined_east": True,
    "south_undefined_south": False,
    "south_undefined_west": True,
    "south_undefined_in": True,
    "south_undefined_out": True,
    "south_north_undefined": False,
    "south_north_north": False,
    "south_north_east": False,
    "south_north_south": False,
    "south_north_west": False,
    "south_north_in": False,
    "south_north_out": False,
    "south_east_undefined": True,
    "south_east_north": False,
    "south_east_east": False,
    "south_east_south": False,
    "south_east_west": False,
    "south_east_in": False,
    "south_east_out": True,
    "south_south_undefined": False,
    "south_south_north": False,
    "south_south_east": False,
    "south_south_south": False,
    "south_south_west": False,
    "south_south_in": False,
    "south_south_out": False,
    "south_west_undefined": True,
    "south_west_north": False,
    "south_west_east": False,
    "south_west_south": False,
    "south_west_west": False,
    "south_west_in": True,
    "south_west_out": False,
    "south_in_undefined": True,
    "south_in_north": False,
    "south_in_east": True,
    "south_in_south": False,
    "south_in_west": False,
    "south_in_in": False,
    "south_in_out": False,
    "south_out_undefined": True,
    "south_out_north": False,
    "south_out_east": False,
    "south_out_south": False,
    "south_out_west": True,
    "south_out_in": False,
    "south_out_out": False,
    "west_undefined_undefined": False,
    "west_undefined_north": True,
    "west_undefined_east": False,
    "west_undefined_south": True,
    "west_undefined_west": False,
    "west_undefined_in": True,
    "west_undefined_out": True,
    "west_north_undefined": True,
    "west_north_north": False,
    "west_north_east": False,
    "west_north_south": False,
    "west_north_west": False,
    "west_north_in": True,
    "west_north_out": False,
    "west_east_undefined": False,
    "west_east_north": False,
    "west_east_east": False,
    "west_east_south": False,
    "west_east_west": False,
    "west_east_in": False,
    "west_east_out": False,
    "west_south_undefined": True,
    "west_south_north": False,
    "west_south_east": False,
    "west_south_south": False,
    "west_south_west": False,
    "west_south_in": False,
    "west_south_out": True,
    "west_west_undefined": False,
    "west_west_north": False,
    "west_west_east": False,
    "west_west_south": False,
    "west_west_west": False,
    "west_west_in": False,
    "west_west_out": False,
    "west_in_undefined": True,
    "west_in_north": False,
    "west_in_east": False,
    "west_in_south": True,
    "west_in_west": False,
    "west_in_in": False,
    "west_in_out": False,
    "west_out_undefined": True,
    "west_out_north": True,
    "west_out_east": False,
    "west_out_south": False,
    "west_out_west": False,
    "west_out_in": False,
    "west_out_out": False,
    "in_undefined_undefined": False,
    "in_undefined_north": True,
    "in_undefined_east": True,
    "in_undefined_south": True,
    "in_undefined_west": True,
    "in_undefined_in": False,
    "in_undefined_out": False,
    "in_north_undefined": True,
    "in_north_north": False,
    "in_north_east": True,
    "in_north_south": False,
    "in_north_west": False,
    "in_north_in": False,
    "in_north_out": False,
    "in_east_undefined": True,
    "in_east_north": False,
    "in_east_east": False,
    "in_east_south": True,
    "in_east_west": False,
    "in_east_in": False,
    "in_east_out": False,
    "in_south_undefined": True,
    "in_south_north": False,
    "in_south_east": False,
    "in_south_south": False,
    "in_south_west": True,
    "in_south_in": False,
    "in_south_out": False,
    "in_west_undefined": True,
    "in_west_north": True,
    "in_west_east": False,
    "in_west_south": False,
    "in_west_west": False,
    "in_west_in": False,
    "in_west_out": False,
    "in_in_undefined": False,
    "in_in_north": False,
    "in_in_east": False,
    "in_in_south": False,
    "in_in_west": False,
    "in_in_in": False,
    "in_in_out": False,
    "in_out_undefined": False,
    "in_out_north": False,
    "in_out_east": False,
    "in_out_south": False,
    "in_out_west": False,
    "in_out_in": False,
    "in_out_out": False,
    "out_undefined_undefined": False,
    "out_undefined_north": True,
    "out_undefined_east": True,
    "out_undefined_south": True,
    "out_undefined_west": True,
    "out_undefined_in": False,
    "out_undefined_out": False,
    "out_north_undefined": True,
    "out_north_north": False,
    "out_north_east": False,
    "out_north_south": False,
    "out_north_west": True,
    "out_north_in": False,
    "out_north_out": False,
    "out_east_undefined": True,
    "out_east_north": True,
    "out_east_east": False,
    "out_east_south": False,
    "out_east_west": False,
    "out_east_in": False,
    "out_east_out": False,
    "out_south_undefined": True,
    "out_south_north": False,
    "out_south_east": True,
    "out_south_south": False,
    "out_south_west": False,
    "out_south_in": False,
    "out_south_out": False,
    "out_west_undefined": True,
    "out_west_north": False,
    "out_west_east": False,
    "out_west_south": True,
    "out_west_west": False,
    "out_west_in": False,
    "out_west_out": False,
    "out_in_undefined": False,
    "out_in_north": False,
    "out_in_east": False,
    "out_in_south": False,
    "out_in_west": False,
    "out_in_in": False,
    "out_in_out": False,
    "out_out_undefined": False,
    "out_out_north": False,
    "out_out_east": False,
    "out_out_south": False,
    "out_out_west": False,
    "out_out_in": False,
    "out_out_out": False,
}

is_cs_lh_unambiguous = {
    "undefined_undefined_undefined": False,
    "undefined_undefined_north": False,
    "undefined_undefined_east": False,
    "undefined_undefined_south": False,
    "undefined_undefined_west": False,
    "undefined_undefined_in": False,
    "undefined_undefined_out": False,
    "undefined_north_undefined": False,
    "undefined_north_north": False,
    "undefined_north_east": True,
    "undefined_north_south": False,
    "undefined_north_west": True,
    "undefined_north_in": True,
    "undefined_north_out": True,
    "undefined_east_undefined": False,
    "undefined_east_north": True,
    "undefined_east_east": False,
    "undefined_east_south": True,
    "undefined_east_west": False,
    "undefined_east_in": True,
    "undefined_east_out": True,
    "undefined_south_undefined": False,
    "undefined_south_north": False,
    "undefined_south_east": True,
    "undefined_south_south": False,
    "undefined_south_west": True,
    "undefined_south_in": True,
    "undefined_south_out": True,
    "undefined_west_undefined": False,
    "undefined_west_north": True,
    "undefined_west_east": False,
    "undefined_west_south": True,
    "undefined_west_west": False,
    "undefined_west_in": True,
    "undefined_west_out": True,
    "undefined_in_undefined": False,
    "undefined_in_north": True,
    "undefined_in_east": True,
    "undefined_in_south": True,
    "undefined_in_west": True,
    "undefined_in_in": False,
    "undefined_in_out": False,
    "undefined_out_undefined": False,
    "undefined_out_north": True,
    "undefined_out_east": True,
    "undefined_out_south": True,
    "undefined_out_west": True,
    "undefined_out_in": False,
    "undefined_out_out": False,
    "north_undefined_undefined": False,
    "north_undefined_north": False,
    "north_undefined_east": True,
    "north_undefined_south": False,
    "north_undefined_west": True,
    "north_undefined_in": True,
    "north_undefined_out": True,
    "north_north_undefined": False,
    "north_north_north": False,
    "north_north_east": False,
    "north_north_south": False,
    "north_north_west": False,
    "north_north_in": False,
    "north_north_out": False,
    "north_east_undefined": True,
    "north_east_north": False,
    "north_east_east": False,
    "north_east_south": False,
    "north_east_west": False,
    "north_east_in": False,
    "north_east_out": True,
    "north_south_undefined": False,
    "north_south_north": False,
    "north_south_east": False,
    "north_south_south": False,
    "north_south_west": False,
    "north_south_in": False,
    "north_south_out": False,
    "north_west_undefined": True,
    "north_west_north": False,
    "north_west_east": False,
    "north_west_south": False,
    "north_west_west": False,
    "north_west_in": True,
    "north_west_out": False,
    "north_in_undefined": True,
    "north_in_north": False,
    "north_in_east": True,
    "north_in_south": False,
    "north_in_west": False,
    "north_in_in": False,
    "north_in_out": False,
    "north_out_undefined": True,
    "north_out_north": False,
    "north_out_east": False,
    "north_out_south": False,
    "north_out_west": True,
    "north_out_in": False,
    "north_out_out": False,
    "east_undefined_undefined": False,
    "east_undefined_north": True,
    "east_undefined_east": False,
    "east_undefined_south": True,
    "east_undefined_west": False,
    "east_undefined_in": True,
    "east_undefined_out": True,
    "east_north_undefined": True,
    "east_north_north": False,
    "east_north_east": False,
    "east_north_south": False,
    "east_north_west": False,
    "east_north_in": True,
    "east_north_out": False,
    "east_east_undefined": False,
    "east_east_north": False,
    "east_east_east": False,
    "east_east_south": False,
    "east_east_west": False,
    "east_east_in": False,
    "east_east_out": False,
    "east_south_undefined": True,
    "east_south_north": False,
    "east_south_east": False,
    "east_south_south": False,
    "east_south_west": False,
    "east_south_in": False,
    "east_south_out": True,
    "east_west_undefined": False,
    "east_west_north": False,
    "east_west_east": False,
    "east_west_south": False,
    "east_west_west": False,
    "east_west_in": False,
    "east_west_out": False,
    "east_in_undefined": True,
    "east_in_north": False,
    "east_in_east": False,
    "east_in_south": True,
    "east_in_west": False,
    "east_in_in": False,
    "east_in_out": False,
    "east_out_undefined": True,
    "east_out_north": True,
    "east_out_east": False,
    "east_out_south": False,
    "east_out_west": False,
    "east_out_in": False,
    "east_out_out": False,
    "south_undefined_undefined": False,
    "south_undefined_north": False,
    "south_undefined_east": True,
    "south_undefined_south": False,
    "south_undefined_west": True,
    "south_undefined_in": True,
    "south_undefined_out": True,
    "south_north_undefined": False,
    "south_north_north": False,
    "south_north_east": False,
    "south_north_south": False,
    "south_north_west": False,
    "south_north_in": False,
    "south_north_out": False,
    "south_east_undefined": True,
    "south_east_north": False,
    "south_east_east": False,
    "south_east_south": False,
    "south_east_west": False,
    "south_east_in": True,
    "south_east_out": False,
    "south_south_undefined": False,
    "south_south_north": False,
    "south_south_east": False,
    "south_south_south": False,
    "south_south_west": False,
    "south_south_in": False,
    "south_south_out": False,
    "south_west_undefined": True,
    "south_west_north": False,
    "south_west_east": False,
    "south_west_south": False,
    "south_west_west": False,
    "south_west_in": False,
    "south_west_out": True,
    "south_in_undefined": True,
    "south_in_north": False,
    "south_in_east": False,
    "south_in_south": False,
    "south_in_west": True,
    "south_in_in": False,
    "south_in_out": False,
    "south_out_undefined": True,
    "south_out_north": False,
    "south_out_east": True,
    "south_out_south": False,
    "south_out_west": False,
    "south_out_in": False,
    "south_out_out": False,
    "west_undefined_undefined": False,
    "west_undefined_north": True,
    "west_undefined_east": False,
    "west_undefined_south": True,
    "west_undefined_west": False,
    "west_undefined_in": True,
    "west_undefined_out": True,
    "west_north_undefined": True,
    "west_north_north": False,
    "west_north_east": False,
    "west_north_south": False,
    "west_north_west": False,
    "west_north_in": False,
    "west_north_out": True,
    "west_east_undefined": False,
    "west_east_north": False,
    "west_east_east": False,
    "west_east_south": False,
    "west_east_west": False,
    "west_east_in": False,
    "west_east_out": False,
    "west_south_undefined": True,
    "west_south_north": False,
    "west_south_east": False,
    "west_south_south": False,
    "west_south_west": False,
    "west_south_in": True,
    "west_south_out": False,
    "west_west_undefined": False,
    "west_west_north": False,
    "west_west_east": False,
    "west_west_south": False,
    "west_west_west": False,
    "west_west_in": False,
    "west_west_out": False,
    "west_in_undefined": True,
    "west_in_north": True,
    "west_in_east": False,
    "west_in_south": False,
    "west_in_west": False,
    "west_in_in": False,
    "west_in_out": False,
    "west_out_undefined": True,
    "west_out_north": False,
    "west_out_east": False,
    "west_out_south": True,
    "west_out_west": False,
    "west_out_in": False,
    "west_out_out": False,
    "in_undefined_undefined": False,
    "in_undefined_north": True,
    "in_undefined_east": True,
    "in_undefined_south": True,
    "in_undefined_west": True,
    "in_undefined_in": False,
    "in_undefined_out": False,
    "in_north_undefined": True,
    "in_north_north": False,
    "in_north_east": False,
    "in_north_south": False,
    "in_north_west": True,
    "in_north_in": False,
    "in_north_out": False,
    "in_east_undefined": True,
    "in_east_north": True,
    "in_east_east": False,
    "in_east_south": False,
    "in_east_west": False,
    "in_east_in": False,
    "in_east_out": False,
    "in_south_undefined": True,
    "in_south_north": False,
    "in_south_east": True,
    "in_south_south": False,
    "in_south_west": False,
    "in_south_in": False,
    "in_south_out": False,
    "in_west_undefined": True,
    "in_west_north": False,
    "in_west_east": False,
    "in_west_south": True,
    "in_west_west": False,
    "in_west_in": False,
    "in_west_out": False,
    "in_in_undefined": False,
    "in_in_north": False,
    "in_in_east": False,
    "in_in_south": False,
    "in_in_west": False,
    "in_in_in": False,
    "in_in_out": False,
    "in_out_undefined": False,
    "in_out_north": False,
    "in_out_east": False,
    "in_out_south": False,
    "in_out_west": False,
    "in_out_in": False,
    "in_out_out": False,
    "out_undefined_undefined": False,
    "out_undefined_north": True,
    "out_undefined_east": True,
    "out_undefined_south": True,
    "out_undefined_west": True,
    "out_undefined_in": False,
    "out_undefined_out": False,
    "out_north_undefined": True,
    "out_north_north": False,
    "out_north_east": True,
    "out_north_south": False,
    "out_north_west": False,
    "out_north_in": False,
    "out_north_out": False,
    "out_east_undefined": True,
    "out_east_north": False,
    "out_east_east": False,
    "out_east_south": True,
    "out_east_west": False,
    "out_east_in": False,
    "out_east_out": False,
    "out_south_undefined": True,
    "out_south_north": False,
    "out_south_east": False,
    "out_south_south": False,
    "out_south_west": True,
    "out_south_in": False,
    "out_south_out": False,
    "out_west_undefined": True,
    "out_west_north": True,
    "out_west_east": False,
    "out_west_south": False,
    "out_west_west": False,
    "out_west_in": False,
    "out_west_out": False,
    "out_in_undefined": False,
    "out_in_north": False,
    "out_in_east": False,
    "out_in_south": False,
    "out_in_west": False,
    "out_in_in": False,
    "out_in_out": False,
    "out_out_undefined": False,
    "out_out_north": False,
    "out_out_east": False,
    "out_out_south": False,
    "out_out_west": False,
    "out_out_in": False,
    "out_out_out": False,
}


def is_cs_well_defined(handedness, directions):
    """Check if the axis directions yield an unambiguous definition right handed"""
    keyword = f"{directions[0]}_{directions[1]}_{directions[2]}"
    if handedness == "right_handed_cartesian":
        if keyword in is_cs_rh_unambiguous:
            if is_cs_rh_unambiguous[keyword] is True:
                return True
    if handedness == "left_handed_cartesian":
        if keyword in is_cs_lh_unambiguous:
            if is_cs_lh_unambiguous[keyword] is True:
                return True
    return False
