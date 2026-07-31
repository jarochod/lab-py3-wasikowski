# R154. Moduł os oraz przydatne funkcje do operowania na plikach oraz katalogach

### Wykład
print("\nWykład\n")

import os

# Ustal lokalizację katalogu, w którym znajduje się aktualny skrypt
script_dir = os.path.dirname(__file__)
print("script_dir =", script_dir)

# Utwórz plik 'test.txt' w tym katalogu i zapisz dane z polskimi znakami (UTF-8)
fh = open(script_dir + "/data.txt", "w", encoding="utf-8")
fh.write("Polskie ogonki ąśćńżźłęó.")
fh.close()

# Sprawdz czy plik newData.txt istnieje w lokalizacji 
print("File newData.txt exists:", os.path.exists(script_dir + "/newData.txt"))

if not os.path.exists(script_dir + "/newData.txt") and os.path.exists(script_dir + "/data.txt"):
    os.rename(script_dir + "/data.txt", script_dir + "/newData.txt")

size = os.path.getsize(script_dir + "/newData.txt") # wielkośc pliku
print("size file:", size)

# Sprawdz czy plik newData.txt istnieje w lokalizacji 
print("File newData.txt exists:", os.path.exists(script_dir + "/newData.txt"))

# Sprawdź, czy ścieżka wskazuje na katalog
print("isdir", os.path.isdir(script_dir + "/newData.txt"))

# Sprawdź, czy ścieżka wskazuje na plik
print("isfile", os.path.isfile(script_dir + "/newData.txt"))

# Sprawdź katalog isnieje, jesli nie to tworzy katalog
if not os.path.exists(script_dir + "/subDir"):
    os.mkdir(script_dir + "/subDir")

# Sprawdź katalog isnieje, jesli tak, to kasuje ten katalog
if os.path.exists(script_dir + "/subDir"):
    os.rmdir(script_dir + "/subDir")

os.remove(script_dir + "/newData.txt")

print()
# Sprawdz katalog roboczy
print("katalog roboczy przed zmianą", os.getcwd())

# Zmień katalog roboczy na katalog skryptu
os.chdir(script_dir)
print("Katalog roboczy po zmianie", os.getcwd())


### Wykład - ćwiczenia
print("\nWykład - ćwiczenia\n")

import os  # Moduł do operacji systemowych: pliki, katalogi, ścieżki
import shutil  # Moduł do zaawansowanych operacji na plikach, jak kopiowanie

# Ustal lokalizację katalogu, w którym znajduje się aktualny skrypt
scriptDir = os.path.dirname(__file__)

# Utwórz plik 'test.txt' w tym katalogu i zapisz dane z polskimi znakami (UTF-8)
fh = open(scriptDir + "/test.txt", "w", encoding="utf-8")
fh.write("Dane ńćśłó")
fh.close()

# Jeśli plik docelowy 'newTest.txt' nie istnieje, zmień nazwę pliku 'test.txt'
if not os.path.exists(scriptDir + "/newTest.txt"):
    os.rename(scriptDir + "/test.txt", scriptDir + "/newTest.txt")

# Wyświetl rozmiar pliku w bajtach
print(os.path.getsize(scriptDir + "/newTest.txt"))

# Sprawdź, czy ścieżka wskazuje na plik
print(os.path.isfile(scriptDir + "/newTest.txt"))

# Sprawdź, czy ścieżka wskazuje na katalog
print(os.path.isdir(scriptDir + "/newTest.txt"))

# Sprawdź, czy istnieje folder 'basics' w bieżącym katalogu
print(os.path.isdir("./basics"))

# Usuń katalog 'subDir', jeśli istnieje
if os.path.exists(scriptDir + "/subDir"):
    os.rmdir(scriptDir + "/subDir")

# Utwórz katalog 'subDir', jeśli nie istnieje
if not os.path.exists(scriptDir + "/subDir"):
    os.mkdir(scriptDir + "/subDir")

# Usuń plik 'newTest.txt', jeśli istnieje
if os.path.exists(scriptDir + "/newTest.txt"):
    os.remove(scriptDir + "/newTest.txt")

# Wyświetl aktualny katalog roboczy
print("current working dir: ", os.getcwd())

# Zmień katalog roboczy na katalog skryptu
os.chdir(scriptDir)
print("current working dir: ", os.getcwd())

# Jeśli nie istnieje kopia pliku 'data.dat', wykonaj jego kopię pod nazwą 'data-copy.dat'
if not os.path.exists("data-copy.dat"):
    shutil.copyfile("data.dat", "data-copy.dat")