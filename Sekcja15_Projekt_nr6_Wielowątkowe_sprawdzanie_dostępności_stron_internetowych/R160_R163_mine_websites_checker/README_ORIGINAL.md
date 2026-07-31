# Multi-threaded Website Status Checker (Wersja 1 – checkUrl w klasie Client)

## 📌 Opis

Ten projekt służy do sprawdzania statusów HTTP stron internetowych z pliku tekstowego. Program działa wielowątkowo, przyspieszając sprawdzanie poprzez równoległe żądania. Logika walidacji i zapytania znajduje się w klasie `Client`.

## 📁 Struktura

```
.
├── main.py
├── websites.py
├── websites.txt
└── report.txt
```

## ⚙️ Schemat działania

1. `websites.txt` zawiera listę domen (np. `google.com`).
2. `Websites` wczytuje dane do listy.
3. W `main.py` tworzone są wątki (`Client`), każdy pobiera dane do sprawdzenia.
4. `Client.checkUrl()` sprawdza status HTTP i walidację URL.
5. Wyniki zapisywane są do raportu `report.txt`.

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

### Client (wbudowana logika)

```
+----------------------------+
|          Client            |
+----------------------------+
| - threadName               |
| - websites                 |
| - sleepTime                |
+----------------------------+
| + __init__()               |
| + run()                    |
| + checkUrl()              <- tutaj jest logika
+----------------------------+
```
