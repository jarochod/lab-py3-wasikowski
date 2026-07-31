# R142. __name__ i funkcja reload

# Moduły -  __name__ wskazuje nazwę modułu lub __main__ (główny plik naszego programu

# W mathModule.py __name__ wskaże na “mathModule”, ale __name__ w głównym programie,
# czyli punktem wejściowym naszego programu będzie wartość:  __main__

import random

def addNumbers(a,b):
    print("mathModule: " + __name__)
    return a + b


print(__name__, "random int:", random.randint(0, 100) ) # __main__ random int: 52