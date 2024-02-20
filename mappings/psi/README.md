# PSI Readme

This directory contains mappings for PSI data files from the PEARL beamline of the Swiss Light Source.
At the time of writing, the application definition for nxmpes is under development.
Given the various scan scripts in use at PEARL, it may be necessary to write a specific conversion tool 
or a _reader_ for the pynxtools converter.
For a first exploration, we concenctrate on the conversion of two specific data files
and using the dataconverter tool with the json_map reader and static mappings.

The two example files are:

- pshell-20200207-174512-XPSSpectrum.h5: A plain and simple spectrum from the Scienta analyser
- pshell-20201022-182802-HoloScan.h5: A two-axes angle scan.

## Files in this directory

### nxmpes.mapping.json

nxmpes mapping template produced by the dataconverter tool.

### mpes-required-fields.txt

Required fields from nxmpes.mapping.json.

### nxmpes.pearl.json

Instrument description of the PEARL endstation that is common for all data files.
These are typically entries that are constant and equal in all mappings.
This file can be copied as a starting point of a new mapping file.

### nxmpes.pearl.defaults.json

Values that are missing in some of the pshell data files.
This file can be copied, filled with actual values, and used as the first input-file to dataconverter.

### nxmpes.XPSSpectrum.mapping.json

Bottom-up assembly of a mapping file for XPSSpectrum data.
The mapping produces a valid Nexus file with minimum requirements.
It does, however, not convert all possible data contained in the original file.

The mapping is tested on pshell-20200207-174512-XPSSpectrum.h5 using the following command line:

```shell
dataconverter --input-file ../pynxtools/mappings/psi/nxmpes.XPSSpectrum.mapping.json
              --input-file pshell-20200207-174512-XPSSpectrum.h5
              --reader json_map
              --nxdl NXmpes
              --output pshell-20200207-174512-XPSSpectrum.nxs
```

### nxmpes.HoloScan.mapping.json

Bottom-up assembly of a mapping file for HoloScan data.
The mapping produces a valid Nexus file with minimum requirements.
It does, however, not convert all possible data contained in the original file.

The mapping is tested on pshell-20201022-182802-HoloScan.h5 using the following command line:

```shell
/home/muntwiler_m/miniconda3/envs/nexpy/bin/python -m pynxtools.dataconverter.convert
    --input-file ../pynxtools/mappings/psi/nxmpes.HoloScan.mapping.json
    --input-file pshell-20201022-182802-HoloScan.h5
    --reader json_map
    --nxdl NXmpes
    --output pshell-20201022-182802-HoloScan.nxs
```

### pearl-nexus-hierarchy.txt

Informal draft of an all-inclusive Nexus file hierarchy for PEARL data files.
