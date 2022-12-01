import requests
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("XDOS by serialfuzzer")
print(ascii_banner)


def XDOSCheck(uri):
    print(f"Testing for {uri}")
    initialStatusCode = requests.get(uri).status_code
    i = 0
    while i < 10000:
        status_code = requests.get(uri).status_code
        if status_code != initialStatusCode:
            print(f"Possible DOS at {uri} after {i} requests")
            break
        i+=1


if len(sys.argv) > 1:
        url = sys.argv[2]
        XDOSCheck(url)
else:
    if not sys.stdin.isatty():
        for line in sys.stdin:
            XDOSCheck(line.rstrip())
    else:
        print("URLs not provided")
