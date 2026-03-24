#!/usr/bin/env python3
import argparse
import re
import sys
import os

# Set up the command-line argument parser
parser = argparse.ArgumentParser()

# Create a mutually exclusive group so only one option can be chosen at a time
group = parser.add_mutually_exclusive_group(required=True)

# Add an option to print sources when the --sources flag is used
group.add_argument("--sources", action="store_true")

# Add an option to print the family name when the --family flag is used
group.add_argument("--family", action="store_true")

# Parse the command-line arguments provided by the user
args = parser.parse_args()

# Read the configuration file from the "sources" directory
with open(os.path.join("sources", "config-Obvia.yaml")) as config:
    data = config.read()

# If the --family flag is specified, attempt to extract the familyName from the config file
if args.family:
    # Search for a line that starts with "familyName:" and capture its value
    m = re.search(r"(?m)^familyName: (.*)", data)
    if m:
        # If a match is found, print the captured family name
        print(m[1])
        sys.exit(0)
    else:
        # If no match is found, print an error message
        print("Could not determine family name from config file!")
        sys.exit(1)

# If the --sources flag is specified, attempt to extract the list of sources
toggle = False
sources = []
for line in data.splitlines():
    # Check if the line marks the beginning of the sources section
    if re.match("^sources:", line):
        toggle = True
        continue
    if toggle:
        # Match each source entry in the YAML list (lines starting with "-")
        m = re.match(r"^\s*-\s*(.*)", line)
        if m:
            # Add each source path with "sources/" prefix
            sources.append("sources/" + m[1])
        else:
            # If the line does not match a source entry, end the sources section
            toggle = False

# If sources were found, print them all in one line
if sources:
    print(" ".join(sources))
    sys.exit(0)  # Exit successfully
else:
    # If no sources were found, print an error message
    print("Could not determine sources from config file!")
    sys.exit(1)  # Exit with error code
