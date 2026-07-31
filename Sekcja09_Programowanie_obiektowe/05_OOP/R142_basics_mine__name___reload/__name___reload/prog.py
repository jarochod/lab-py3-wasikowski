# R142. __name__ i funkcja reload

# Moduły -  __name__ wskazuje nazwę modułu lub __main__ (główny plik naszego programu

# W mathModule.py __name__ wskaże na “mathModule”, ale __name__ w głównym programie,
# czyli punktem wejściowym naszego programu będzie wartość:  __main__

import mathModule  # mathModule random int: 56
import importlib

print( mathModule.addNumbers(10,2) ) # mathModule: mathModule
                                     # 12
print( "prog.py: " + __name__ ) # prog.py: __main__


# Moduły - reload() 
# Każdy import wykonuje kod z zaimportowanego pliku
# Istnieje możliwość ponownego importu modułu i wykonanie jego kodu dzięki modułowi importlib i metody reload()

importlib.reload(mathModule)
importlib.reload(mathModule)
importlib.reload(mathModule)
