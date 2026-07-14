#!/usr/bin/env python3

import sys
import json
import os
import urllib.request

cwd = os.path.dirname(os.path.abspath(__file__))
arg = sys.argv

with open(os.path.join(cwd, '.version'), 'r') as f:
    version = json.loads(f.read())

ext_ver = json.loads(urllib.request.urlopen('').read())

if version['version'] != ext_ver['version']:
    print(f"An update for Sparkle is available. ({version} -> {ext_ver})")
else:
    print("Sparkle is up to date!")