# R147. Prosty odczyt z pliku

# Aby otworzyć plik trzeba użyć metodę open, przekazać ścieżkę do pliku oraz tryb otwarcia pliku, funkcja
# zwraca uchwyt do pliku na bazie, którego można wykonywać różne operacje.


# Tryby otwarcia pliku:
#  r - otwarcie pliku tylko do odczytu
#  rb - odczyt pliku w formacie binarnym
#  w - plik otwarty do zapisu, zanim będzie zapis na początku treść pliku jest usuwana
#  a - otwarcie pliku do zapisu, dodanie treści na koniec pliku, czyli treść nie jest kasowana
#  Dodanie + powoduje otwarcie pliku zarówno do odczytu i zapisu np r+ (odczyt i zapis)

from pathlib import Path

# 1. Ścieżka do pliku (zastępuje zwykłe "test.txt")
BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "data" / "output"
file_path = OUTPUT_DIR / "test.txt"

# 2. Bezpieczny odczyt z automatycznym zamykaniem pliku
with open(file_path, "r", encoding="utf-8") as fh:
    lines = fh.readlines()

# 3. Wypisanie linii w pętli (rstrip usuwa podwójne znaki nowej linii przy print)
for line in lines:
    print(line.rstrip())
