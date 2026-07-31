# Multi-threaded Website Status Checker (Version 3 – checkUrl in Websites)

## 📌 Description

In this version, the logic for checking each website (URL validation and HTTP request) is moved into the `Websites` class. This keeps the `Client` class minimal and delegates all website-related operations to a single class.

## 📁 Structure

```
.
├── main.py
├── websites.py    <-- with checkUrl method
├── websites.txt
└── report.txt
```

## ⚙️ How it works

1. `websites.txt` provides a list of domains to check.
2. The `Websites` class loads the data and defines `checkUrl()`.
3. `main.py` runs `Client` threads, which pull entries and pass them to `websites.checkUrl()`.
4. Results are returned and saved into the report.

## 🧩 Class and Method Diagram

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
| + checkUrl(data: dict)    |
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
