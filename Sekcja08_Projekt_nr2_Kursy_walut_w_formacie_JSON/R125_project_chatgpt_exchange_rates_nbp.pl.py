# R125. Projekt nr. 2 Kursy walut w formacie JSON

import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")

if response.ok:
    data = response.json()[0]  # Pobieramy pierwszy element listy
    rates = data["rates"]
    base = "PLN"  # NBP podaje kursy w odniesieniu do PLN
    date = data["effectiveDate"]

    print(f"Base currency: {base}")
    print(f"Date: {date}")

    for rate in rates: # Iteracja po rates
        print(f"{rate['code']} ({rate['currency']}): {rate['mid']} PLN") # Każdy element w rates to słownik. Odczytujemy code, currency i mid.
