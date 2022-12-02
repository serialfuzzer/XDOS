import requests
import sys
import pyfiglet

debug = False
ascii_banner = pyfiglet.figlet_format("XDOS by serialfuzzer")
print(ascii_banner)


def XDOSCheck(uri):
    print(f"Testing for {uri}")
    response = requests.get(uri)
    initialStatusCode = response.status_code
    i = 0
    while i < 10000:
        resp = requests.get(uri)
        status_code = resp.status_code
        if debug == True:
            print(f"Request Number: {i+1}, Status Code: {status_code}, Response Length: { len(resp.content) } ")
        if status_code != initialStatusCode:
            print(f"Possible DOS at {uri} after {i} requests")
            break
        i+=1


if len(sys.argv) > 1:
        url = sys.argv[1]
        XDOSCheck(url)
else:
    if not sys.stdin.isatty():
        for line in sys.stdin:
            XDOSCheck(line.rstrip())
    else:
        print("URLs not provided")
