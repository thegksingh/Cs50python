import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argumnet")

try:
    amount = float(sys.argv[1])
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=11e214bb1397e50c910f34f2a2c5c483e6b35beae6bff0b29d4e144be04c50a7"
    result = requests.get(url)
    result.raise_for_status()
    try:
        data = result.json()
        price = float(data["data"]["priceUsd"])
        cost = price * amount
        print(f"${cost}")
    except requests.RequestException:
        sys.exit()
except ValueError:
    sys.exit("Command-line argumnet is not a number")
