# R148. Ścieżki do plików absolutne i relatywne

# Ścieżki plików - Plik file1.txt pojawił się w aktualnym folderze na którym wykonuje się
#  skrypt Pythona tzw. current working directory czyli w moim przypadku:
# D:\Projekty\Projekty_VSC\Python\Python_PL_KW_\

### Wykład
print("\nWykład\n")

import os

print("path to script __file__: ", __file__) # absolutna ścieżka do skryptu
script_dir = os.path.dirname(__file__) # absol. ścieżka do katalogu skryptu
print("script located in folder, script_dir:", script_dir) 

# ścieżka absolutna na którym katalogu skrypt jest wykonywany
print("current working directory: os.getcwd(): ", os.getcwd()) # current working directory: os.getcwd():  
# D:\Projekty\Projekty_VSC\Python\Python_PL_KW_

fh = open("file1.txt", "w")
fh.write("content")  
fh.close()  


### Wykład - ćwiczenia
print("\nWykład - ćwiczenia\n")

import os

print("Absolute path to script file", __file__)
scriptDir = os.path.dirname(__file__)
print("Absolute path to script directory: ", scriptDir)

pathToFile = scriptDir + "\\newFile.txt"
print("Path to file:", pathToFile)

fh = open(pathToFile, "w")
fh.write("content!")
fh.close()

