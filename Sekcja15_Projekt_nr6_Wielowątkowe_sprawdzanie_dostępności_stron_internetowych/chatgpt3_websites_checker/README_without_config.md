# 🧵 Wielowątkowy Sprawdzacz Statusu Stron WWW (wersja modułowa bez config.py)

## 📌 Opis

Ten projekt sprawdza status HTTP listy stron internetowych przy użyciu wielu wątków. Wykorzystuje podejście modułowe, w którym logika została rozdzielona do osobnych plików. Klasa `Client` zawiera lokalną blokadę wątku (Lock), a `UrlChecker` odpowiada za walidację adresów URL oraz wykonywanie zapytań HTTP.

## 📁 Struktura plików

```
project/
├── main.py
├── websites.py
├── client.py
├── url_checker.py
├── websites.txt
└── report.txt
```


## ⚙️ Jak to działa

1. `websites.txt` zawiera listę nazw domen.
2. `websites.py` obsługuje wczytywanie pliku oraz zapis raportu.
3. `client.py` definiuje klasę `Client`, która używa `UrlChecker` do walidacji i pobierania statusu.
4. `main.py` uruchamia wiele wątków (`Client`).
5. `url_checker.py` realizuje walidację URL i wysyła zapytania HTTP przy użyciu bibliotek `validators` i `requests`.

## 🧩 Przegląd klas

### Websites

- `__init__(filename)` – inicjalizuje klasę i ładuje plik
- `loadFile(filename)` – przetwarza strony na listę wewnętrzną
- `getNextWebsiteToCheck()` – zwraca kolejny element do przetworzenia (bezpieczne w głównym wątku)
- `putWebsiteData(data)` – dodaje przetworzone dane do raportu
- `saveReport()` – zapisuje raport do pliku `report.txt`

### Client (wątek)

- `__init__(threadName, websites, sleepTime)`
- `run()` – pobiera dane URL i przetwarza je przy użyciu `UrlChecker`

### UrlChecker

- `check(data: dict)` – waliduje i pobiera status HTTP

