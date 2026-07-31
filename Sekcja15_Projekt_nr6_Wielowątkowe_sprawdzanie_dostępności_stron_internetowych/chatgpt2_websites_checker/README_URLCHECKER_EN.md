# Multi-threaded Website Status Checker (Version 2 – with UrlChecker class)

## 📌 Description

This version separates responsibilities more cleanly. The `Client` class handles only threading and task control, while the `UrlChecker` class encapsulates URL validation and HTTP request logic. This makes the code more readable, testable, and modular.

## 📁 Structure

```
.
├── main.py
├── websites.py
├── url_checker.py
├── websites.txt
└── report.txt
```

## ⚙️ How it works

1. `websites.txt` contains a list of websites.
2. The `Websites` class loads the input and manages the report.
3. `main.py` creates and starts 10 `Client` threads.
4. Each `Client` gets data and passes it to `UrlChecker.check()`.
5. `UrlChecker` validates the URL and performs an HTTP request.
6. Results are added to the report list and saved to `report.txt`.

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
+---------------------------+
```

### UrlChecker

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
