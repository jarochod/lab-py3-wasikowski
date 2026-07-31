# 🧵 Wielowątkowy Sprawdzacz Statusu Stron WWW (wersja modułowa z folderem `pack/`)

## 📌 Opis

Ten projekt sprawdza statusy HTTP stron internetowych z listy, korzystając z wielu wątków. Cała logika aplikacji została umieszczona w pakiecie `pack/`. Globalna blokada wątków (`dataLock`) jest zdefiniowana w `config.py` i współdzielona między modułami.

## 📁 Struktura projektu

```
project/
├── main.py
├── websites.txt
└── pack/
    ├── __init__.py
    ├── client.py
    ├── config.py
    ├── url_checker.py
    └── websites.py
```

## ⚙️ Jak to działa

1. `websites.txt` zawiera listę stron do sprawdzenia.
2. `main.py` jest punktem startowym, który uruchamia wiele wątków.
3. Każdy wątek `Client` korzysta z `UrlChecker`, aby sprawdzić statusy HTTP.
4. Dostęp do współdzielonych danych jest chroniony za pomocą `dataLock` z `config.py`.

## 🧩 Przegląd klas

### Websites
- `__init__(filename)` – wczytuje i przechowuje listę stron
- `getNextWebsiteToCheck()` – zwraca kolejną stronę (bezpieczne dla wątków)
- `putWebsiteData(data)` – zapisuje wyniki
- `saveReport()` – zapisuje raport końcowy do `report.txt`

### Client
- `__init__(threadName, websites, sleepTime)`
- `run()` – pętla wątku przetwarzająca strony przez `UrlChecker`

### UrlChecker
- `check(data: dict)` – waliduje adresy URL i pobiera status HTTP

### config
- `dataLock` – globalna blokada do bezpiecznego dostępu wielowątkowego
