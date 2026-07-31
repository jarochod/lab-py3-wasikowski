# R125. Projekt nr. 2 Kursy walut w formacie JSON

import requests

base = "USD"
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format=json")

if response.ok == True:
    data = response.json()
    print(data)
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print("base: " + base)
    print("date: " + date)
    #print(rates)

    for key in rates:
        print(key + ": ", rates[key])