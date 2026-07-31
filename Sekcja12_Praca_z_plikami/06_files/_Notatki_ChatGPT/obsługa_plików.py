
# 1) Otwieranie plików w Pythonie
# fh = open("nazwa_pliku.txt", "tryb")
fh = open("nazwa_pliku.txt", "w")
# Zwraca uchwyt do pliku, który można wykorzystać do operacji (np. odczyt/zapis).

# 2) Tryby otwierania plików:
# "r"   - Odczyt (read). Błąd, jeśli plik nie istnieje.
# "w"   - Zapis (write). Tworzy nowy plik lub nadpisuje istniejący.
# "a"   - Dopisywanie (append). Dodaje dane na końcu pliku.
# "r+"  - Odczyt i zapis, bez kasowania zawartości.
# "w+"  - Zapis i odczyt. Kasuje zawartość pliku przy otwarciu.
# "a+"  - Dopisywanie i odczyt. Zapis dodawany na końcu.
# "rb" / "wb" - Operacje binarne (odczyt/zapis).

# 3) Zapis do pliku
fh = open("test.txt", "w")
fh.write("To jest test.\n")
fh.write("Druga linia.")
fh.close()

# 4) Odczyt z pliku
fh = open("test.txt", "r")
content = fh.read()
print(content)
fh.close()

# 5) Lepsza metoda: with open
with open("test.txt", "r") as fh:
    for line in fh:
        print(line.strip())

# 6) Inne metody operacji na plikach:
# read()      - Odczytuje cały plik jako jeden ciąg znaków.
# readline()  - Czyta jedną linię z pliku.
# readlines() - Zwraca listę wszystkich linii.
# write()     - Zapisuje dane do pliku (ciąg znaków).
# writelines(lista) - Zapisuje listę ciągów znaków do pliku.

# 7) Ścieżki relatywne i absolutne
fh = open("dane/test.txt", "r")  # relatywna ścieżka
fh = open("C:/Users/Kuba/Desktop/python/test.txt", "r")  # absolutna ścieżka

# 8) Informacje o ścieżkach
import os
print("Aktualna ścieżka pliku:", __file__)
print("Folder skryptu:", os.path.dirname(__file__))
print("Bieżący katalog roboczy:", os.getcwd())

# 9) Try - Except dla obsługi błędów
try:
    with open("file1.txt", "w") as fh:
        fh.write("content")
except:
    print("Wystąpił błąd wejścia/wyjścia.")

# 10) Wylistowanie zawartości folderów
print(os.listdir("."))           # aktualny katalog
print(os.listdir("./basics"))    # podfolder basics
print(os.listdir(".."))          # katalog wyżej
print(os.listdir("../programs")) # katalog wyżej + programs

# 11) Sprawdzenie istnienia pliku
if os.path.exists("test.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

# 12) Obsługa wyjątków przy odczycie
try:
    with open("plik.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie został znaleziony.")
except IOError:
    print("Błąd wejścia/wyjścia.")

# 13) Iteracja po liniach pliku
with open("plik.txt", "r") as f:
    for line in f:
        print(line.strip())

# 14) Odczyt pliku binarnego
with open("image.png", "rb") as f:
    data = f.read()

# 15) Ustawienie kodowania przy odczycie pliku
with open("plik.txt", "r", encoding="utf-8") as f:
    print(f.read())
