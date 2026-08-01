# R146. Wstęp do pracy z plikami. Zapis do pliku

# Obsługa plików - odczyt plików to podstawowa umiejętność każdego programisty. Pliki konfiguracyjne,
# tekstowe czy bardziej zaawansowane bazy danych pozwalają na przechowywanie danych dla naszych programów.
# Aby otworzyć plik trzeba użyć metodę open, przekazać ścieżkę do pliku oraz tryb otwarcia pliku, funkcja
# zwraca uchwyt do pliku na bazie, którego można wykonywać różne operacje.


# Tryby otwarcia pliku:
#  r - otwarcie pliku tylko do odczytu
#  rb - odczyt pliku w formacie binarnym
#  w - plik otwarty do zapisu, zanim będzie zapis na początku treść pliku jest usuwana
#  a - otwarcie pliku do zapisu, dodanie treści na koniec pliku, czyli treść nie jest kasowana
#  Dodanie + powoduje otwarcie pliku zarówno do odczytu i zapisu np r+ (odczyt i zapis)

from pathlib import Path

# R146. Wstęp do pracy z plikami. Zapis do pliku

# 1. Wyznaczenie głównego katalogu projektu (lab-py3-wasikowski)
BASE_DIR = Path(__file__).resolve().parents[2]

# 2. Ścieżka do folderu wyjściowego
OUTPUT_DIR = BASE_DIR / "data" / "output"

# 3. Zdefiniowanie pełnej ścieżki do pliku test.txt w folderze output
file_path = OUTPUT_DIR / "test.txt"

# 4. Zapis do pliku (tryb 'w' - tworzy lub nadpisuje)
with open(file_path, "w", encoding="utf-8") as fh:
    fh.write("content1\n")
    fh.write("content2\n")

# 5. Dopisywanie do pliku (tryb 'a' - append)
with open(file_path, "a", encoding="utf-8") as fh2:
    fh2.write("content3\n")

