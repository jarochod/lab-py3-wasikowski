# R151. Odczyt pliku tekstowego z polskimi ogonkami w standardzie UTF-8

# Odczyt pliku z kodowaniem UTF - 8 - praca z polskimi ogonkami czy innymi specyficznymi znakami 
# wymaga skorzystania z kodowania znaków w standardzie UTF-8, dzięki temu unikniemy dziwacznych 
# symboli przy próbie zapisu takich znaków.

print("\nWykład")
import os

path = __file__ # # absol. ścieżka do bieżącego pliku .py
print(path)

print()
script_dir = os.path.dirname(__file__) # # absol. ścieżka do katalogu skryptu
print("script located in folder, script_dir:", script_dir)  


fh = open(script_dir+"/ogonki_.txt", "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

print()
for line in lines:
    print(line.rstrip())



fh = open(script_dir + "/ogonki_.txt", "r", encoding="utf-8")

while True:
    line = fh.readline()
    if not line:
        break
    print(line.rstrip())
    
fh.close()


print()
with open(script_dir + "/ogonki_.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        print(line.rstrip())



print("\nĆwiczenia")
import os

scriptDir = os.path.dirname(__file__)

fh = open(scriptDir + "/ogonki.txt", "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

print(lines)
print()
for line in lines:
    print(line.rstrip())


fh = open(scriptDir + "/ogonki.txt", "r", encoding="utf-8")
print()
while True:
    line = fh.readline()
    if not line:
        break
    print(line.rstrip())

fh.close()



# Wczytanie danych pliku naraz, jako jeden string.
# Używaj with i fh.read(), jeśli chcesz tylko szybko podejrzeć zawartość pliku lub masz mały plik.
with open(scriptDir + "/ogonki.txt", "r", encoding="utf-8") as fh:
    print(fh.read())

# Wczytanie danych pliku linia po linii.
# Używaj with i for line in fh: + rstrip(), jeśli zależy Ci na czystym i kontrolowanym wypisywaniu linii 
# – to podejście jest też bardziej uniwersalne i wydajne przy dużych plikach.
with open(scriptDir + "/ogonki.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        print(line.rstrip())


