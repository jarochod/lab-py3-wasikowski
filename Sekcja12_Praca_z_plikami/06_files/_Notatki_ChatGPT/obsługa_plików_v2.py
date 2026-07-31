
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
fh = open("test.txt", "w")
fh.write("To jest test.\n")
fh.write("Druga linia.")
fh.close()

# Odczyt z pliku
fh = open("test.txt", "r")
content = fh.read()
print(content)
fh.close()

# Lepsza metoda: with open
with open("test.txt", "r") as fh:
    for line in fh:
        print(line.strip())

# Inne metody operacji na plikach:
# read()      - Odczytuje cały plik jako jeden ciąg znaków.
# readline()  - Czyta jedną linię z pliku.
# readlines() - Zwraca listę wszystkich linii.
# write()     - Zapisuje dane do pliku (ciąg znaków).
# writelines(lista) - Zapisuje listę ciągów znaków do pliku.

# Ścieżki relatywne i absolutne
fh = open("dane/test.txt", "r")  # relatywna ścieżka
fh = open("d:\\Projekty\\Projekty_VSC\\Python\\Python_PL_KW_\\Sekcja12_Praca_z_plikami\\basics\\06_files\\test.txt", "r")  # absolutna ścieżka
import os
print("Aktualna ścieżka pliku:", __file__)
print("Folder skryptu:", os.path.dirname(__file__))
print("Bieżący katalog roboczy:", os.getcwd())

# Try - Except dla obsługi błędów
try:
    with open("file1.txt", "w") as fh:
        fh.write("content")
except:
    print("Wystąpił błąd wejścia/wyjścia.")

# Wylistowanie zawartości folderów
print(os.listdir("."))           # aktualny katalog
print(os.listdir("./Sekcja01_Wstep"))    # podfolder basics
print(os.listdir(".."))          # katalog wyżej
print(os.listdir("../Python_PL_KW")) # katalog wyżej + programs

# Sprawdzenie istnienia pliku
if os.path.exists("test.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

# Obsługa wyjątków przy odczycie
try:
    with open("plik.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie został znaleziony.")
except IOError:
    print("Błąd wejścia/wyjścia.")

# Iteracja po liniach pliku
with open("plik.txt", "r") as f:
    for line in f:
        print(line.strip())

# Odczyt pliku binarnego
with open("image.png", "rb") as f:
    data = f.read()

# Ustawienie kodowania przy odczycie pliku
with open("plik.txt", "r", encoding="utf-8") as f:
    print(f.read())
