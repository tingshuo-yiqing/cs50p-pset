import requests
import sys


arvg = sys.argv

if len(arvg) < 2:
    sys.exit("Missing command-line argument")
elif len(arvg) == 2:
    try:
        count = float(arvg[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    repose = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=e90b70ff5e0c28a0900167f6d7b2e9faea7758cc1edb5ae07a7b0ffdddf6ccb0',
                        )
    contxt = repose.json()
    price = float(contxt["data"]["priceUsd"]) * count
    print(f"{price:,.4f}$")
except requests.RequestException:
    pass