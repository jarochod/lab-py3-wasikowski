# R155_basics__file_exception.py

# Obsługa wyjątków - dodatkowo można wskazać konkretny wyjątek, który ma być obsłużony np. IOError
# dla błędów podczas pracy z plikami.

import os  # import modułu os (operacje na ścieżkach, plikach itp.)

script_dir = os.path.dirname(__file__)  # pobiera ścieżkę katalogu, w którym znajduje się uruchamiany plik skryptu
print(script_dir)  # wyświetla absolutną ścieżkę do katalogu skryptu

fh = None  # zmienna dla uchwytu do pliku (ang. file handle)

try:
    # próba otwarcia pliku 'test.txt' w trybie zapisu ("w") w folderze skryptu
    fh = open(script_dir + "/test.txt", "w")
    fh.write("content")  # zapisanie tekstu do pliku
except IOError:
    # obsługa błędu wejścia/wyjścia (np. brak uprawnień, błąd zapisu)
    print("Wystąpił błąd wejścia/wyjścia (IOError)")
else:
    # jeśli nie wystąpił żaden wyjątek — zamknij plik i poinformuj użytkownika
    print("Zamykam plik")
    fh.close()

# Jest oobsługa błędu IOError jeśli zaistnieje. 
# Jeśli nie ma błedu, to błędu  po else  zostanie zamknięty dostęp do pliku

#####

"""
# Z pliku Python+-+PDF.pdf

 import os
 # sometimes script runs in different folder
 # from where it is located
 script_dir = os.path.dirname(__file__)
 print(script_dir) # absolute path to runned script
 fh = None
 try: 
    fh = open(script_dir + "/test.txt", "w")
    fh.write("content")
 except IOError:
    print("IOError occured" )
 else: 
    print("closing file")
    fh.close()

"""