import requests
from pprint import pprint

base_url = "https://zenquotes.io/api/random"
quotes = requests.get(base_url)

if quotes.status_code == 200:
    quotes = quotes.json()
    pprint(quotes)
else:
    print(f"Error: {quotes.status_code}")
