from models.user import User
from models.employee import Employee
from models.manager import Manager

def test_people():
    print("\n🔹 Tworzę użytkownika (User)")
    u = User("Ala")

    print("\n🔹 Tworzę pracownika (Employee)")
    e = Employee("Bartek")

    print("\n🔹 Tworzę menedżera (Manager)")
    m = Manager("Celina")

    print("\n✅ Obiekty utworzone, wypisuję je:")
    print(u)
    print(e)
    print(m)

if __name__ == "__main__":
    test_people()
