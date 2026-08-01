# R149. Listowanie plików katalogu i relatywne ścieżki


# Ścieżki plików - podsumowując ścieżka do pliku skryptu  pythona, a katalog w którym jest on
# uruchomiony to dwie różne rzeczy, dlatego trzeba mieć to na uwadze.
# Prosty kod pozwala na wylistowanie plików w folderze w którym wykonywany jest domyślnie program:

print("\nWykład\n")
import os
# . to aktualny katalog czyli folder bieżący, gdzie wykonuje się program
# . to też ścieżka relatywna/względna
arr = os.listdir(".")
print(arr)

# ścieżka absolutna na którym katalogu skrypt jest wykonywany
print("current working directory: os.getcwd(): ", os.getcwd()) # current working directory: os.getcwd():  /home/jaro/dev/learning/lab-py3-wasikowski



# Wylistowanie zawartości folderów
# import os
# print(os.listdir("."))                # aktualny katalog
# print(os.listdir("./Sekcja01_Wstep")) # podfolder Sekcja01_Wstep
# print(os.listdir(".."))               # katalog wyżej
# print(os.listdir("../lab-py3-wasikowski"))  # katalog wyżej + lab-py3-wasikowski


print("\nćwiczenia")
# Wylistowanie zawartości folderów i ścieżka relatywna/względna
import os

print()
print("Current working directory: ", os.getcwd() )

print()
files = os.listdir(".")
print(files) # current working dir

print()
files = os.listdir("./Sekcja12_Praca_z_plikami")
print(files) # ['basics', 'challenges', 'obsługa_plików.md', 'obsługa_plików.py', 'obsługa_plików_2.md', 'obsługa_plików_v2.py', 'Temp']

print()
files = os.listdir("./Sekcja12_Praca_z_plikami/06_files")
print(files)

print()
dir = os.listdir("..") # katalog wyżej względem current working dir
print(dir)

print()
files = os.listdir("../lab-py3-wasikowski")
print(files) # ['.git', '.gitignore', 'basics', 'challenges']



print("\nĆwiczenia2")
import os

print()
getcwd = os.getcwd()
print("Current working directory:", getcwd)

print()
dir = os.listdir(".")
print(dir)

print()
dir = os.listdir("..")
print(dir)

