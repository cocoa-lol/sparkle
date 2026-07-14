#!/usr/bin/env python3

import sys
import json
import os
import urllib.request

def main():
    cwd = os.path.dirname(os.path.abspath(__file__))
    arg = sys.argv[1:]
    ext_ver = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/.version').read())
    pkgs = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/.packages').read().decode('utf-8'))
    # Load local .version file
    with open(os.path.join(cwd, '.version'), 'r') as f:
        version = json.loads(f.read())
    with open(os.path.join(cwd, '.packages')) as f:
        local_pkgs 
    # Check for updates
    if version['version'] != ext_ver['version']:
        print(f"An update for Sparkle is available. ({version} -> {ext_ver})")
    else:
        print("Sparkle is up to date!")

    # Begin sparkle
    print(pkgs)
    print(arg)
    if arg[0] == "install":
        if arg[1] in pkgs:
            print('Found package')
        else:
            sys.exit("Could not find package: " + arg[1])
    elif arg[0] == "update-packages":
        print("Updating packages..")
        with open(os.path.join(cwd, ".packages"), "w") as f:
            o