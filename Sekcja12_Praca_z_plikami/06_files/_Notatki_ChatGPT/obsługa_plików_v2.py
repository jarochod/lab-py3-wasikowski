
# Otwieranie plików w Pythonie
# fh = open("nazwa_pliku.txt", "tryb")
# Zwraca uchwyt do pliku, który można wykorzystać do operacji (np. odczyt/zapis).

# Tryby otwierania plików:
# "r"   - Odczyt (read). Błąd, jeśli plik nie istnieje.
# "w"   - Zapis (write). Tworzy nowy plik lub nadpisuje istniejący.
# "a"   - Dopisywanie (append). Dodaje dane na końcu pliku.
# "r+"  - Odczyt i zapis, bez kasowania zawartości.
# "w+"  - Zapis i odczyt. Kasuje zawartość pliku przy otwarciu.
# "a+"  - Dopisywanie i odczyt. Zapis dodawany na końcu.
# "rb" / "wb" - Operacje binarne (odczyt/zapis).

# Zapis do pliku
fh = open("data/output/test.txt", "w")
fh.write("To jest test.\n")
fh.write("Druga linia.")
fh.close()

# Odczyt z pliku
fh = open("data/output/test.txt", "r")
content = fh.read()
print(content)
fh.close()

# Lepsza metoda: with open
with open("data/output/test.txt", "r") as fh:
    for line in fh:
        print(line.strip())

# Inne metody operacji na plikach:
# read()      - Odczytuje cały plik jako jeden ciąg znaków.
# readline()  - Czyta jedną linię z pliku.
# readlines() - Zwraca listę wszystkich linii.
# write()     - Zapisuje dane do pliku (ciąg znaków).
# writelines(lista) - Zapisuje listę ciągów znaków do pliku.

# Ścieżki relatywne i absolutne
fh = open("data/input/test.txt", "r")  # relatywna ścieżka
fh = open("/home/jaro/dev/learning/lab-py3-wasikowski/data/input/test.txt", "r")  # absolutna ścieżka
import os
print("Aktualna ścieżka pliku:", __file__)
print("Folder skryptu:", os.path.dirname(__file__))
print("Bieżący katalog roboczy:", os.getcwd())

# Try - Except dla obsługi błędów
try:
    with open("data/output/test.txt", "w") as fh:
        fh.write("content")
except:
    print("Wystąpił błąd wejścia/wyjścia.")

# Wylistowanie zawartości folderów
print(os.listdir("."))           # aktualny katalog
print(os.listdir("./Sekcja01_Wstep"))    # podfolder basics
print(os.listdir(".."))          # katalog wyżej
print(os.listdir("../lab-py3-wasikowski")) # katalog wyżej + programs

# Sprawdzenie istnienia pliku
if os.path.exists("data/output/test.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

# Obsługa wyjątków przy odczycie
try:
    with open("data/output/test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie został znaleziony.")
except IOError:
    print("Błąd wejścia/wyjścia.")

# Iteracja po liniach pliku
with open("data/output/test.txt", "r") as f:
    for line in f:
        print(line.strip())

# Odczyt pliku binarnego
with open("data/input/image.png", "rb") as f:
    data = f.read()

# Ustawienie kodowania przy odczycie pliku
with open("data/output/test.txt", "r", encoding="utf-8") as f:
    print(f.read())
