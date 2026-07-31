# R150. Zapis pliku tekstowego z polskimi ogonkami w standardzie UTF-8

# Zapis pliku z kodowaniem UTF-8 - praca z polskimi ogonkami czy innymi specyficznymi znakami 
# wymaga skorzystania z kodowania znaków w standardzie UTF-8, dzięki temu unikniemy dziwacznych 
# symboli przy próbie zapisu takich znaków

print("\nWykład\n")

import os

script_dir = os.path.dirname(__file__) # # absol. ścieżka do katalogu skryptu
print("script located in folder, script_dir:", script_dir) 

fh = open(script_dir + "/ogonki_.txt", "w", encoding="utf-8")
fh.write("Małe polskie ogonki: ą, ć, ę, ł, ń, ó, ś, ź, ż.\n")  
fh.write("Duże polskie ogonki: Ą, Ć, Ę, Ł, Ń, Ó, Ś, Ź, Ż.")  
fh.close() 



print("\nćwiczenia\n")

import os

scriptDir = os.path.dirname(__file__)
print(scriptDir)

fh = open( scriptDir + "/ogonki.txt", "w" , encoding="utf-8" )
fh.write("tekst z ogonkami: ąśół\n")
fh.write("tekst z ogonkami: ąśół\n")
fh.write("tekst z ogonkami: ąśół\n")
fh.close()