#!/usr/bin/env python3
from sh import git
import datetime
import re
import sys
from urllib.parse import quote
import subprocess
import requests

# Constants for base repository and URLs
BASE_OWNER = "googlefonts"
BASE_REPONAME = "googlefonts-project-template"
DUMMY_URL = "https://yourname.github.io/your-font-repository-name"
LATEST_OFL = "https://raw.githubusercontent.com/googlefonts/googlefonts-project-template/main/OFL.txt"

# Helper functions
def repo_url(owner, name):
    # Construct and return the GitHub repository URL
    return f"https://github.com/{owner}/{name}"

def web_url(owner, name):
    # Construct and return the GitHub Pages URL for the project
    return f"https://{owner}.github.io/{name}"

def lose(msg, e=None):
    # Print an error message and exit if initialization fails
    print(msg)
    print("You will need to do the initialization steps manually.")
    print("Read scripts/customize.py for more instructions on how to do this.")
    if e:
        # If an exception object is provided, print additional diagnostic info
        print("\nHere's an additional error message which may help diagnose the problem.")
        raise e
    # Exit the program with error code
    sys.exit(1)

# Try to get the repository URL from the local git configuration
try:
    # Attempt to retrieve the URL of the 'origin' remote
    my_repo_url = git.remote("get-url", "origin")
except Exception as e:
    # If an error occurs, call the lose() function to print an error message and exit
    lose("Could not use git to find my own repository URL", e)

# Parse repository owner and name from the repository URL
m = re.match(r"(?:https://github.com/|git@github.com:)(.*)/(.*)/?", str(my_repo_url))
if not m:
    # If the URL does not match the expected GitHub format, exit with an error
    lose(f"My git repository URL ({my_repo_url}) didn't look what I expected - are you hosting this on github?")

# Extract the repository owner and name from the regex match
owner, reponame = m[1], m[2]

# Prevent running the script on the upstream template repository
if owner == BASE_OWNER and reponame == BASE_REPONAME:
    print("I am being run on the upstream repository; don't do that")
    sys.exit()

# Fix URLs in README to point to the user's repository instead of the template
readme = open("README.md").read()

# Construct the correct GitHub Pages and repository URLs for the user's repo
ghpages_url = web_url(owner, reponame)
project_url = repo_url(owner, reponame)

# Replace the template GitHub Pages URL with the user's actual URL
print("Fixing URLs:", web_url(BASE_OWNER, BASE_REPONAME), "->", ghpages_url)
readme = readme.replace(web_url(BASE_OWNER, BASE_REPONAME), ghpages_url)

# Fix encoded URLs in badges (e.g., CI/CD status badges that use URL encoding)
readme = readme.replace(
    quote(web_url(BASE_OWNER, BASE_REPONAME), safe=""),
    quote(web_url(owner, reponame), safe=""),
)

# Replace dummy placeholder URL with the user's actual GitHub Pages URL
print("Fixing URLs:", DUMMY_URL, "->", ghpages_url)
readme = readme.replace(f"`{DUMMY_URL}`", ghpages_url)

# Write the updated README content back to the file
with open("README.md", "w") as fh:
    fh.write(readme)

# Stage the modified README file in git for commit
git.add("README.md")

# Get the current year
year = datetime.date.today().year

# Convert the repository name to title case for display
title = reponame.title()

# Construct the copyright line with year, project title, and repository URL
copyright = f"Copyright {year} The {title} Project Authors ({project_url})\n"

print("Fetching the latest OFL..")

# Download the latest OFL license text from the official source
ofl = requests.get(LATEST_OFL).text.splitlines()

print("Writing an OFL for you")
print(copyright)

# Write the customized OFL file: first the copyright line, then the rest of the license
with open("OFL.txt", "w") as fh:
    fh.write(copyright)
    fh.write("\n".join(ofl[1:]))

# Stage the new OFL file in git for commit
git.add("OFL.txt")

# Pin dependencies for reproducible builds
print("Pinning dependencies")

# Run 'pip freeze' to capture the exact versions of installed dependencies
dependencies = subprocess.check_output(["pip", "freeze"])

# Write the dependency list to requirements.txt for consistent builds
with open("requirements.txt", "wb") as dependency_file:
    dependency_file.write(dependencies)

# Stage the requirements.txt file in git for commit
git.add("requirements.txt")

# Commit and push changes if any modifications were made
result = git.status("--porcelain")

# Check if there are any modified files (lines starting with "M ")
if any(line.startswith("M ") for line in result.splitlines()):
    # Commit the changes with a descriptive message
    git.commit("-m", "Customize repository")
    print("Pushing changes to GitHub")
    git.push()
else:
    # If no changes were detected, skip committing and pushing
    print("Nothing changed, no need to push")
