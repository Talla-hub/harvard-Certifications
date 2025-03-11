import requests
import json
import sys
try:
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    url="https://api.coindesk.com/v1/bpi/currentprice.json"
    response=requests.get(url)
    response =response.json()
    bit=float(sys.argv[1]) * float(response["bpi"]["USD"]["rate_float"])
    print(f"${bit:,.4f}")
except (requests.RequestException,ValueError):
    sys.exit("command-line argument is not a number")
