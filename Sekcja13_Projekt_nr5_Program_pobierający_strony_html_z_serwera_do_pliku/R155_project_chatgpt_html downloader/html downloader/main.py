import os
import sys
import urllib.parse
import validators  # pip install validators
import requests
from datetime import datetime

# Wypisanie informacji o argumentach wejściowych
print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments list: {sys.argv}")

# Domyślny URL
default_url = "https://duckduckgo.com"
url = sys.argv[1] if len(sys.argv) > 1 else default_url

print(f"Website to download: {url}")

# Parsowanie URL i sprawdzenie, czy zawiera protokół
if not urllib.parse.urlparse(url).scheme:
    url = "https://" + url  # Automatyczne dodanie protokołu https

# Sprawdzenie, czy URL jest poprawny
if not validators.url(url):
    print(f"Url: {url} is invalid")
    sys.exit("Bad URL!")

# Pobranie katalogu skryptu (w razie uruchamiania jako plik .py)
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print(f"Current working dir: {os.getcwd()}")

# Utworzenie katalogu na pobrane strony
websites_dir = os.path.join(script_dir, "websites")
os.makedirs(websites_dir, exist_ok=True)

# Próba pobrania strony
try:
    response = requests.get(url, allow_redirects=True, timeout=10)
    response.raise_for_status()  # Wywoła wyjątek, jeśli kod odpowiedzi HTTP >= 400
except requests.exceptions.RequestException as e:
    print(f"Error downloading URL: {e}")
    sys.exit(1)

print(f"Response ok from server for url: {url}")

# Utworzenie nazwy pliku
now = datetime.now()
date_string = now.strftime("%d.%m.%Y %H.%M.%S")
parsed_url = urllib.parse.urlparse(url)
file_name = f"{parsed_url.netloc} {date_string}.html"
file_path = os.path.join(websites_dir, file_name)

# Zapis zawartości do pliku
try:
    with open(file_path, "wb") as fh:
        fh.write(response.content)
    print(f"Website saved to: {file_path}")
except IOError as e:
    print(f"Error saving file: {e}")
    sys.exit(1)
