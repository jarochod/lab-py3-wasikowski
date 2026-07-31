# R125. Projekt nr. 2 Kursy walut w formacie JSON

import requests

# Adres API
access_key = "86d1dba3bc059566bec5da9db2b153f5"
url = f"https://api.exchangeratesapi.io/v1/latest?access_key={access_key}"

# Wysłanie zapytania do API
response = requests.get(url)

# Sprawdzenie czy zapytanie zakończyło się sukcesem
if response.ok:
    data = response.json()
    
    if data["success"]:
        base = data["base"]
        date = data["date"]
        rates = data["rates"]

        print(f"Base currency: {base}")
        print(f"Date: {date}")

        for code, rate in rates.items():
            print(f"{code}: {rate} {base}")

    else:
        print("Error in API response.")
else:
    print(f"HTTP request failed with status code {response.status_code}")