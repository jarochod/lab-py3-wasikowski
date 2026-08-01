import os

# Utworzenie wymaganych katalogów, jeśli nie istnieją
os.makedirs("data/input", exist_ok=True)
os.makedirs("data/output", exist_ok=True)

# 1) Otwieranie plików w Pythonie
# fh = open("data/output/nazwa_pliku.txt", "w")
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
fh = open("data/output/test.txt", "w", encoding="utf-8")
fh.write("To jest test.\n")
fh.write("Druga linia.")
fh.close()

# 4) Odczyt z pliku
fh = open("data/output/test.txt", "r", encoding="utf-8")
content = fh.read()
print(content)
fh.close()

# 5) Lepsza metoda: with open
with open("data/output/test.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        print(line.strip())

# 6) Inne metody operacji na plikach:
# read()      - Odczytuje cały plik jako jeden ciąg znaków.
# readline()  - Czyta jedną linię z pliku.
# readlines() - Zwraca listę wszystkich linii.
# write()     - Zapisuje dane do pliku (ciąg znaków).
# writelines(lista) - Zapisuje listę ciągów znaków do pliku.

# 7) Ścieżki relatywne i absolutne
# Przykład odczytu z wejścia (data/input):
if not os.path.exists("data/input/test.txt"):
    with open("data/input/test.txt", "w", encoding="utf-8") as f:
        f.write("Przykładowe dane wejściowe")

fh = open("data/input/test.txt", "r", encoding="utf-8")  # ścieżka relatywna
fh.close()

# Przykładowa ścieżka absolutna (dostosuj do swojego systemu):
# fh = open("C:/Users/Kuba/Desktop/python/data/input/test.txt", "r")

# 8) Informacje o ścieżkach
print("Aktualna ścieżka pliku:", __file__)
print("Folder skryptu:", os.path.dirname(__file__))
print("Bieżący katalog roboczy:", os.getcwd())

# 9) Try - Except dla obsługi błędów
try:
    with open("data/output/file1.txt", "w", encoding="utf-8") as fh:
        fh.write("content")
except IOError:
    print("Wystąpił błąd wejścia/wyjścia.")

# 10) Wylistowanie zawartości folderów
print("Zawartość katalogu roboczego:", os.listdir("."))
if os.path.exists("./Sekcja01_Wstep"):
    print("Zawartość Sekcja01_Wstep:", os.listdir("./Sekcja01_Wstep"))
print("Zawartość data/output:", os.listdir("data/output"))

# 11) Sprawdzenie istnienia pliku
if os.path.exists("data/output/test.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")

# 12) Obsługa wyjątków przy odczycie
try:
    with open("data/output/plik.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik 'data/output/plik.txt' nie został znaleziony.")
except IOError:
    print("Błąd wejścia/wyjścia.")

# 13) Iteracja po liniach pliku
with open("data/output/test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 14) Odczyt pliku binarnego (tworzymy atrapę obrazka, jeśli nie istnieje)
if not os.path.exists("data/input/image.png"):
    with open("data/input/image.png", "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")  # Nagłówek PNG

with open("data/input/image.png", "rb") as f:
    data = f.read()
    print("Odczytano bajtów z pliku binarnego:", len(data))

# 15) Ustawienie kodowania przy odczycie pliku
with open("data/output/test.txt", "r", encoding="utf-8") as f:
    print(f.read())
