# 🧵 Wielowątkowy Sprawdzacz Statusu Stron WWW (wersja modułowa z config.py)

## 📌 Opis

Ta wersja projektu używa globalnej blokady `dataLock`, zapisanej w osobnym pliku `config.py`. Zwiększa to modularność i upraszcza synchronizację między wątkami w wielu plikach. Reszta projektu pozostaje zgodna z zasadą oddzielenia logiki do osobnych modułów.

## 📁 Struktura plików

```
project/
├── main.py
├── websites.py
├── client.py
├── url_checker.py
├── config.py
├── websites.txt
└── report.txt
```

## ⚙️ Jak to działa

1. `websites.txt` zawiera listę stron do sprawdzenia.
2. `websites.py` wczytuje dane i generuje raport.
3. `url_checker.py` sprawdza poprawność adresów URL i wysyła zapytania HTTP.
4. `client.py` definiuje klasę wątku `Client`, korzystającą z `dataLock` zaimportowanego z `config.py`.
5. `config.py` udostępnia współdzieloną blokadę globalną wykorzystywaną zarówno w `main.py`, jak i `client.py`.
6. `main.py` tworzy i uruchamia wiele wątków `Client`.

## 🔐 Dlaczego `config.py`?

Przeniesienie `dataLock` do `config.py` sprawia, że wszystkie wątki korzystają z tej samej współdzielonej blokady. Zapewnia to bezpieczny dostęp do wspólnych danych bez konieczności tworzenia wielu instancji Lock.

## 🧩 Przegląd klas

### Websites

- `__init__(filename)` – ładuje listę stron
- `getNextWebsiteToCheck()` – bezpieczne odczytywanie danych
- `putWebsiteData(data)` – zapisuje wynik
- `saveReport()` – zapisuje raport do pliku

### Client

- `__init__(threadName, websites, sleepTime)`
- `run()` – synchronizuje działania za pomocą `dataLock` z `config.py`

### UrlChecker

- `check(data: dict)` – sprawdza URL (walidacja + zapytanie HTTP)
