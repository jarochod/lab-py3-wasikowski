# R141. Moduły instrukcja import oraz from import
# Moduły - instrukcja import

# Instrukcja import importuje jako moduł dowolny kod z innego pliku. Funkcja addNumbers w 
# mathModule.py jest zaimportowana do moduleTest.py i użyta jako mathModule.addNumbers(3,8)

# Instrukcja import pozwala na import wielu modułów po przecinku za jednym razem:

import mathModule, random

print( mathModule.addNumber(3, 8) )
print( random.randint(0, 100))

# Moduł jest importowany tylko raz niezależnie ile razy była wywołana instrukcja import