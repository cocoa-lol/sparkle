#!/usr/bin/env python3

import sys
import json
import os
import urllib.request

cwd = os.path.dirname(os.path.abspath(__file__))
arg = sys.argv[1:]
ext_ver = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/.version').read())
pkgs = urllib.request.urlopen('').read()
# Load local .version file
with open(os.path.join(cwd, '.version'), 'r') as f:
    version = json.loads(f.read())

# Check for updates
if version['version'] != ext_ver['version']:
    print(f"An update for Sparkle is available. ({version} -> {ext_ver})")
else:
    print("Sparkle is up to date!")

# Begin sparkle
print(arg)
if arg[0] == "install":
    if arg[1] in pkgs:
        pass
    else:
        sys.exit("Could not find package: " + arg[1])