# 🧵 Multi-threaded Website Status Checker (modular version with config.py)

## 📌 Description

This version of the project uses a global `dataLock` stored in a separate `config.py` file. It improves modularity and simplifies thread synchronization across files. The rest of the design follows clean separation of logic between files.

## 📁 File Structure

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

## ⚙️ How it Works

1. `websites.txt` is the input list of websites.
2. `websites.py` reads and stores site data and generates the report.
3. `url_checker.py` checks URL validity and sends HTTP requests.
4. `client.py` defines the `Client` thread class, using `dataLock` from `config.py`.
5. `config.py` provides a shared global lock used in both `main.py` and `client.py`.
6. `main.py` creates and joins multiple `Client` threads.

## 🔐 Why `config.py`?

By moving the `dataLock` to `config.py`, all threads use the same shared lock. This ensures safe concurrent access to shared data without creating multiple lock instances.

## 🧩 Class Overview

### Websites

- `__init__(filename)` – loads website list
- `getNextWebsiteToCheck()` – thread-safe read from shared list
- `putWebsiteData(data)` – stores result
- `saveReport()` – writes to report

### Client

- `__init__(threadName, websites, sleepTime)`
- `run()` – synchronized operations using `dataLock` from `config.py`

### UrlChecker

- `check(data: dict)` – performs URL checking (validation + HTTP request)
