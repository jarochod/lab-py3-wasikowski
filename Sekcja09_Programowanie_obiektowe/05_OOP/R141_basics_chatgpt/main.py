from models.user import User
from models.employee import Employee
from models.manager import Manager

def test1_create_people():
    print("🔨 Tworzę obiekty klas:")
    u = User("Ala")
    e = Employee("Bartek")
    m = Manager("Celina")

    print(u)
    print(e)
    print(m)

    return u, e, m

def test2_info_people(people):
    print("\n🔍 Wywołuję metodę info() na wszystkich osobach:")
    for person in people:
        print(f"- {person.info()}")

if __name__ == "__main__":
    u, e, m = test1_create_people()
    test2_info_people([u, e, m])

