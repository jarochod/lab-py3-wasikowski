# Multi-threaded Website Status Checker (Version 1 – checkUrl in Client class)

## 📌 Description

This project checks the HTTP status of websites listed in a text file. It uses multi-threading to speed up the process by making concurrent requests. The validation and request logic is implemented directly in the `Client` class.

## 📁 Structure

```
.
├── main.py
├── websites.py
├── websites.txt
└── report.txt
```

## ⚙️ How it works

1. `websites.txt` contains a list of domain names (e.g., `google.com`).
2. The `Websites` class loads the data into a list.
3. In `main.py`, multiple threads (`Client`) are created. Each thread processes one website at a time.
4. `Client.checkUrl()` validates the URL and sends an HTTP GET request.
5. Results are stored in `report.txt`.

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

### Client

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
| + checkUrl()               |
+----------------------------+
```
