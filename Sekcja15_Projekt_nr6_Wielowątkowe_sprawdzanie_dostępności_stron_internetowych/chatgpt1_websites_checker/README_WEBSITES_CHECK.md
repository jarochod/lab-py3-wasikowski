# Multi-threaded Website Status Checker (Wersja 3 – checkUrl w Websites)

## 📌 Opis

W tej wersji logika sprawdzania stron (walidacja + żądanie HTTP) została przeniesiona do klasy `Websites`. Dzięki temu `Client` skupia się wyłącznie na zarządzaniu wątkiem, a `Websites` odpowiada za całość logiki operacyjnej stron.

## 📁 Struktura

```
.
├── main.py
├── websites.py    <-- z metodą checkUrl
├── websites.txt
└── report.txt
```

## ⚙️ Schemat działania

1. `websites.txt` → lista domen.
2. `Websites` ładuje dane i udostępnia metodę `checkUrl()`.
3. `main.py` uruchamia `Client`, który pobiera dane i przekazuje do `websites.checkUrl()`.
4. Wynik trafia do raportu.

## 🧩 Diagram klas i metod

### Websites (rozszerzona)

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
| + checkUrl(data: dict)    |  <- nowa metoda
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
