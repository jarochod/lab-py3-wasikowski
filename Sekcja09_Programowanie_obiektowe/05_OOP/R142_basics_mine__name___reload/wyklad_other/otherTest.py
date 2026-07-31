# R142. __name__ i funkcja reload

# Każdy import wykonuje kod z zaimportowanego pliku
# Istnieje możliwość ponownego importu modułu i wykonanie jego kodu dzięki 
# modułowi importlib i metody reload()

import random
print( f"random from otherTest.py {random.randint(0, 100)}" )


