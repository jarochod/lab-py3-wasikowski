# Multi-threaded Website Status Checker (Wersja 2 – z klasą UrlChecker)

## 📌 Opis

Ta wersja rozdziela odpowiedzialności: `Client` obsługuje tylko wątek, a logika walidacji i zapytań HTTP znajduje się w osobnej klasie `UrlChecker`. Podejście to zwiększa czytelność i testowalność.

## 📁 Struktura

```
.
├── main.py
├── websites.py
├── url_checker.py
├── websites.txt
└── report.txt
```

## ⚙️ Schemat działania

1. `websites.txt` → lista stron.
2. `Websites` ładuje dane i obsługuje raport.
3. `main.py` tworzy i uruchamia 10 wątków `Client`.
4. Każdy `Client` pobiera dane i wysyła je do `UrlChecker`.
5. `UrlChecker.check()` wykonuje walidację i żądanie HTTP.
6. Wyniki trafiają do `reportList` i są zapisywane.

## 🧩 Diagram klas i metod

### Websites

```
+---------------------------+
|         Websites          |
+---------------------------+
| - filename                |
| - fileList                |
| - reportList              |
| - index                   |
+---------------------------+
| + __init__()              |
| + loadFile()              |
| + getNextWebsiteToCheck() |
| + putWebsiteData()        |
| + saveReport()            |
+---------------------------+
```

### UrlChecker (nowy moduł)

```
+---------------------------+
|        UrlChecker         |
+---------------------------+
| + check(data: dict)       |
+---------------------------+
```

### Client

```
+---------------------------+
|          Client           |
+---------------------------+
| - threadName              |
| - websites                |
| - sleepTime               |
+---------------------------+
| + __init__()              |
| + run()                   |
+---------------------------+
```
