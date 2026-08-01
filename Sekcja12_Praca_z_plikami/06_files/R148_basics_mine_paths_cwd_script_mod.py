# R148. Ścieżki do plików absolutne i relatywne

# Ścieżki plików - Plik test.txt pojawił się w aktualnym folderze na którym wykonuje się
#  skrypt Pythona tzw. current working directory

### Wykład
print("\nWykład\n")

import os

print("path to script __file__: ", __file__) # absolutna ścieżka do skryptu
script_dir = os.path.dirname(__file__) # absol. ścieżka do katalogu skryptu
print("script located in folder, script_dir:", script_dir)

# ścieżka absolutna na którym katalogu skrypt jest wykonywany
print("current working directory: os.getcwd(): ", os.getcwd()) # current working directory: os.getcwd():


fh = open("data/output/test.txt", "w")
fh.write("content")
fh.close()


### Wykład - ćwiczenia
print("\nWykład - ćwiczenia\n")

import os

print("Absolute path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)

pathToFile = scriptDir + "/newFile.txt"
print("Path to file:", pathToFile)

fh = open(pathToFile, "w")
fh.write("content!")
fh.close()


### Mod
print("\nMod\n")

from pathlib import Path

# REKOMENDOWANE PODEJŚCIE (modern Python 3.4+):
# 1. Path(__file__).resolve().parents[2] dynamicznie wyznacza korzeń projektu,
#    dzięki czemu skrypt działa niezależnie od tego, skąd uruchomisz go w terminalu.
# 2. Operator '/' sam dobiera właściwy separator dla systemu (Windows '\' vs Linux '/').
# 3. Blok 'with open' automatycznie dba o zamknięcie pliku bez używania fh.close().

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR / "data" / "output" / "test.txt"

with open(file_path, "w", encoding="utf-8") as fh:
    fh.write("content!")
