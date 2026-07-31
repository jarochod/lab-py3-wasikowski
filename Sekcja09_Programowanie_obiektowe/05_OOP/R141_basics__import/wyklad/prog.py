# R141. Moduły instrukcja import oraz from import
# Moduły - instrukcja from... import

from user import User, Empolyee

user1 = User("Ania", "Kowalska")
print(user1)

employee = Empolyee("Adam", "Kot")
print(employee)

# Instrukcja  from user import *   zaimportowałaby wszystkie elementy z danego modułu.