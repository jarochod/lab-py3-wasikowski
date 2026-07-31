import os, sys  # Moduły do operacji systemowych i argumentów wiersza poleceń
import urllib.parse  # Do rozkładania adresów URL na części
import validators  # Zewnętrzna biblioteka do walidacji adresów URL (pip install validators)
import requests  # Biblioteka HTTP do pobierania stron (pip install requests)
from datetime import datetime  # Do obsługi daty i czasu

# Wypisanie liczby i listy argumentów przekazanych do skryptu
print(f"Number of arguments: {len(sys.argv)}")
print(f"Arguments list: {sys.argv}")

# Domyślny URL – DuckDuckGo
url = "https://duckduckgo.com"
# Jeżeli przekazano argument URL, to nadpisujemy wartość domyślną
if len(sys.argv) > 1:
    url = sys.argv[1]

print(f"Website to download: {url}")

# Pobranie katalogu, w którym znajduje się skrypt
scriptDir = os.path.dirname(__file__)
# Ustawienie katalogu roboczego na ten katalog
os.chdir(scriptDir)

print(f"Current working dir: {os.getcwd()}")

# Utworzenie katalogu 'websites', jeśli nie istnieje
if not os.path.exists("./websites"):
    os.mkdir("websites")

# Parsowanie URL – rozbicie go na części (np. protokół, domena, ścieżka itd.)
parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

# Walidacja URL – czy podany adres URL jest poprawny
validFlag = validators.url(url)
if validFlag:
    print(f"Url: {url} is valid")
else:
    print(f"Url: {url} is invalid")
    raise Exception("Bad URL!")  # Przerywamy działanie skryptu, jeśli URL jest błędny

# Wysłanie żądania GET do podanego URL (z obsługą przekierowań)
response = requests.get(url, allow_redirects=True)
if response.ok == True:
    print(f"Response ok from server for url: {url}")
    
    # Pobranie aktualnej daty i czasu
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H.%M.%S")
    print(dateString)
    
    # Przygotowanie nazwy pliku na podstawie domeny i daty
    fileName = f"./websites/{parsedUrl.netloc} {dateString}.html"
    print(fileName)
    
    # Zapis odpowiedzi (HTML strony) do pliku
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
