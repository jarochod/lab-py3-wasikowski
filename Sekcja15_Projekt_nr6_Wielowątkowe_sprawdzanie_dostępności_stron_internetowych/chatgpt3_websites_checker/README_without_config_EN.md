# 🧵 Multi-threaded Website Status Checker (modular version without config.py)

## 📌 Description

This project checks the HTTP status of a list of websites using multiple threads. It uses a modular design where logic is separated into different files. The `Client` class contains a local thread lock, and `UrlChecker` encapsulates URL validation and HTTP request logic.

## 📁 File Structure

```
project/
├── main.py
├── websites.py
├── client.py
├── url_checker.py
├── websites.txt
└── report.txt
```

## ⚙️ How it Works

1. `websites.txt` contains a list of domain names.
2. `websites.py` handles reading from the file and writing to the report.
3. `client.py` defines the `Client` class which uses `UrlChecker` to validate and fetch status.
4. Multiple threads (clients) are launched from `main.py`.
5. `url_checker.py` performs the actual URL checking using `validators` and `requests`.

## 🧩 Class Overview

### Websites

- `__init__(filename)` – initializes and loads file
- `loadFile(filename)` – parses websites into internal list
- `getNextWebsiteToCheck()` – returns next item to process (thread-safe in main)
- `putWebsiteData(data)` – adds processed data to report
- `saveReport()` – writes report to `report.txt`

### Client (Thread)

- `__init__(threadName, websites, sleepTime)`
- `run()` – fetches URL data and processes it using `UrlChecker`

### UrlChecker

- `check(data: dict)` – validates and fetches HTTP status
