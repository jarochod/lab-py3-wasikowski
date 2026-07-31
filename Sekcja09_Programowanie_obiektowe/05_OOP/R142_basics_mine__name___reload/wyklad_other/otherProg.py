# R142. __name__ i funkcja reload

# Każdy import wykonuje kod z zaimportowanego pliku
# Istnieje możliwość ponownego importu modułu i wykonanie jego kodu dzięki 
# modułowi importlib i metody reload()

# import othersTest importuje i wykonuje kod w module
import otherTest # random from otherTest.py 60
import importlib

print("OtherProg test")

# reload importuje wcześniej zaimportowany moduł
importlib.reload(otherTest) # random from otherTest.py 26
importlib.reload(otherTest) # random from otherTest.py 59