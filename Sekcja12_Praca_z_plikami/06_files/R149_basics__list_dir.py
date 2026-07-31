# R149. Listowanie plików katalogu i relatywne ścieżki

import os

print("Current working directory: ", os.getcwd() )

files = os.listdir(".")
#print(files) # current working dir

files = os.listdir("./programs")
#print(files)

files = os.listdir("./basics/05 OOP/cart")
#print(files)

files = os.listdir("../programs")
print(files)
