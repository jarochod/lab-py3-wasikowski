# R141. Moduły instrukcja import oraz from import

import user
from manager import Manager

user1 = user.User("Ola")
print("main:", user1)

employee1 = user.Employee("Adam")
print("main: ", employee1)

manager1 = Manager("Kasia")
print("main: ", manager1)