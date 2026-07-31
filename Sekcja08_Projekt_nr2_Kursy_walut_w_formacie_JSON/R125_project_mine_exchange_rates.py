# R125. Projekt nr. 2 Kursy walut w formacie JSON

import requests

access_key = "86d1dba3bc059566bec5da9db2b153f5"
url = f"https://api.exchangeratesapi.io/v1/latest?access_key={access_key}"

response = requests.get(url)

if response.ok:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print(f"Base currency: {base}")
    print(f"Date: {date}")

    for key, value in rates.items():
        print(f"{key}: {value}")
else:
    print("Failed to retrieve data")




"""
import requests

base = "USD"
response = requests.get("https://api.exchangeratesapi.io/v1/latest?access_key=86d1dba3bc059566bec5da9db2b153f5")

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print("base: " + base)
    print("date: " + date)
    # print(rates)

    for key, value in rates.items():
        print(f"{key}: {value}")

"""





