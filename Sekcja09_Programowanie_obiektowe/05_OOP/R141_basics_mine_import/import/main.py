# R141. Moduły instrukcja import oraz from import

from user import User
from employee import Employee
from manager import Manager


user1 = User("Ala")
print("main:", user1)

employee1 = Employee("Adam")
print("main:", employee1)

manager1 = Manager("Kasia")
print("main:", manager1)






from user import User
from employee import Employee
from manager import Manager

def test_people():
    u = User("Ala")
    e = Employee("Bartek")
    m = Manager("Celina")

    print(u)
    print(e)
    print(m)

# Ten kod wykona się TYLKO jeśli odpalasz plik bezpośrednio
if __name__ == "__main__":
    test_people()
