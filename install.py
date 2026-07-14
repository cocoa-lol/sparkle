from urllib.request import urlopen

def main():
    sparkle = urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/sparkle.py').read().decode('utf-8')
    version = urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/.version').read().decode('utf-8')
    bat = urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/sparkle.bat').read().decode('utf-8')
    pkgs = urlopen('https://raw.githubusercontent.com/cocoa-lol/sparkle/refs/heads/main/src/.packages').read().decode('utf-8')
    
    with open("sparkle.py", "w", encoding="utf-8", newline="") as f:
        f.write(sparkle)
    with open("sparkle.bat", "w", encoding="utf-8", newline="") as f:
        f.write(bat)
    with open(".version", "w", encoding="utf-8", newline="") as f:
        f.write(version)
    with open(".packages", "w", encoding="utf-8", newline="utf-8") as f:
        f.write(pkgs)
if __name__ == "__main__":
    main()