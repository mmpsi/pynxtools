"""This is a code that performs several tests on nexus tool

"""
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

import os
import logging
import xml.etree.ElementTree as ET

from nexusutils.nexus import nexus


def test_get_nexus_classes_units_attributes():
    """Check the correct parsing of a separate list for:
Nexus classes (base_classes)
Nexus units (memberTypes)
Nexus attribute type (primitiveTypes)
the tested functions can be found in nexus.py file
"""

    # Test 1
    nexus_classes_list = nexus.get_nx_classes()

    assert 'NXbeam' in nexus_classes_list

    # Test 2
    nexus_units_list = nexus.get_nx_units()
    assert 'NX_TEMPERATURE' in nexus_units_list

    # Test 3
    nexus_attribute_list = nexus.get_nx_attribute_type()
    assert 'NX_FLOAT' in nexus_attribute_list


def test_nexus(tmp_path):
    """The nexus test function

"""
    local_dir = os.path.abspath(os.path.dirname(__file__))
    example_data = os.path.join(local_dir, '../data/nexus/201805_WSe2_arpes.nxs')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.\
        FileHandler(os.path.join(tmp_path, 'nexus_test.log'), 'w')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    nexus_helper = nexus.HandleNexus(logger, [example_data])
    nexus_helper.process_nexus_master_file(None)

    with open(os.path.join(tmp_path, 'nexus_test.log'), 'r') as logfile:
        log = logfile.readlines()
    with open(os.path.join(local_dir, '../data/nexus/Ref_nexus_test.log'), 'r') as reffile:
        ref = reffile.readlines()

    assert log == ref

    # didn't work with filecmp library
    # log = os.path.join(local_dir, 'data/nexus_test_data/nexus_test.log')
    # ref = os.path.join(local_dir, 'data/nexus_test_data/Ref2_nexus_test.log')
    # print('yoyo', filecmp.cmp(log, ref, shallow=False))

    # print('Testing of nexus.py is SUCCESSFUL.')


def test_get_node_at_nxdl_path():
    """Test to verify if we receive the right XML element for a given NXDL path"""
    local_dir = os.path.abspath(os.path.dirname(__file__))
    nxdl_file_path = os.path.join(local_dir, "../data/dataconverter/NXtest.nxdl.xml")
    elem = ET.parse(nxdl_file_path).getroot()
    node = nexus.get_node_at_nxdl_path("/ENTRY/NXODD_name", elem=elem)
    assert node.attrib["type"] == "NXdata"
    assert node.attrib["name"] == "NXODD_name"

    node = nexus.get_node_at_nxdl_path("/ENTRY/NXODD_name/float_value", elem=elem)
    assert node.attrib["type"] == "NX_FLOAT"
    assert node.attrib["name"] == "float_value"
