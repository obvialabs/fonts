#!/usr/bin/env python3
# Yes, this is a Bad YAML Parser, but at this stage we are not in the
# venv and do not know what modules the user has available, so for
# maximum compatibility, we are just assuming a plain Python distribution.

import argparse
import re
import sys
import os

# Set up command-line argument parser
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--sources", action="store_true")  # Option to print sources
group.add_argument("--family", action="store_true")   # Option to print family name
args = parser.parse_args()

# Read the configuration file from sources directory
with open(os.path.join("sources", "config-Obvia.yaml")) as config:
    data = config.read()

# If --family is specified, extract the familyName from config
if args.family:
    m = re.search(r"(?m)^familyName: (.*)", data)
    if m:
        print(m[1])  # Print the family name
        sys.exit(0)
    else:
        print("Could not determine family name from config file!")
        sys.exit(1)

# If --sources is specified, extract the list of sources
toggle = False
sources = []
for line in data.splitlines():
    if re.match("^sources:", line):
        toggle = True
        continue
    if toggle:
        m = re.match(r"^\s*-\s*(.*)", line)
        if m:
            sources.append("sources/" + m[1])  # Add each source path
        else:
            toggle = False
if sources:
    print(" ".join(sources))  # Print all sources in one line
    sys.exit(0)
else:
    print("Could not determine sources from config file!")
    sys.exit(1)
