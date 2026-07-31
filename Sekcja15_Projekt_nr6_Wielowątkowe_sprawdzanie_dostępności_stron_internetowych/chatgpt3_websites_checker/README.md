
# 🧵 Wielowątkowy Sprawdzacz Statusu Stron Internetowych (wersja modułowa bez config.py)

## 📌 Opis

Ten projekt sprawdza status HTTP listy stron internetowych, wykorzystując wiele wątków. Korzysta z modułowego projektu, gdzie logika jest podzielona na różne pliki. Klasa `Client` zawiera lokalną blokadę wątku, a `UrlChecker` enkapsuluje logikę walidacji URL i żądań HTTP.

## 📁 Struktura Plików

```plaintext
project/
├── main.py
├── websites.py
├── client.py
├── url_checker.py
├── websites.txt
└── report.txt
```

## 🛠️ Wymagania

- Python 3.6 lub nowszy
- Biblioteki: `requests`, `concurrent.futures`

## 🚀 Uruchomienie

1. Sklonuj repozytorium lub pobierz pliki.
2. Upewnij się, że masz zainstalowane wszystkie wymagania.
3. Uruchom `main.py` za pomocą Pythona.

## 🔧 Konfiguracja

- Dodaj swoje strony internetowe do pliku `websites.txt`, każda w nowej linii.
- Wyniki będą zapisywane w pliku `report.txt`.

## 📜 Licencja

Ten projekt jest licencjonowany na zasadach Licencji MIT - zobacz plik LICENSE, aby uzyskać więcej szczegółów.
