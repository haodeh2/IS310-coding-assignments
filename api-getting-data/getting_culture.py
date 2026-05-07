import requests
import json
import pandas as pd
import os

open_library_url = "https://openlibrary.org/search.json?q=pride+and+prejudice"

response = requests.get(open_library_url)

print(response.status_code)

data = response.json()
first_book = data["docs"][0]

print(first_book)

europeana_api_key = os.environ['rionetilbu']

europeana_url = f"https://api.europeana.eu/record/v2/search.json?wskey={europeana_api_key}&query=Jane+Austen"

europeana_response = requests.get(europeana_url)

print(europeana_response.status_code)

europeana_data = europeana_response.json()

print(europeana_data["items"][0])

combined_data = {
    "open_library": first_book,
    "europeana": europeana_data["items"][0]
}

with open("openlibrary_europeana_data.json", "w", encoding="utf-8") as file:
    json.dump(combined_data, file, indent=4)

print("Data saved successfully!")