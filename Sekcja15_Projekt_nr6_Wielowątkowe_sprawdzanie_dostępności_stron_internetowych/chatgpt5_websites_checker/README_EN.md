# 🧵 Multi-threaded Website Status Checker (modular version using `pack/`)

## 📌 Description

This project checks the HTTP status of websites from a list using multiple threads. The core logic is modularized inside a dedicated `pack/` package. A global thread lock (`dataLock`) is defined in `config.py` and shared across modules.

## 📁 Project Structure

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

## ⚙️ How It Works

1. `websites.txt` holds the list of websites to be checked.
2. `main.py` is the entry point that starts multiple threads.
3. Each `Client` thread uses `UrlChecker` to validate and fetch status codes.
4. Shared access to website lists is synchronized using `dataLock` from `config.py`.

## 🧩 Class Overview

### Websites
- `__init__(filename)` – loads and stores the website list
- `getNextWebsiteToCheck()` – gets the next site (thread-safe)
- `putWebsiteData(data)` – stores the result
- `saveReport()` – saves final results to `report.txt`

### Client
- `__init__(threadName, websites, sleepTime)`
- `run()` – thread loop that processes URLs with `UrlChecker`

### UrlChecker
- `check(data: dict)` – validates URLs and fetches HTTP status

### config
- `dataLock` – global threading lock to ensure safe access
