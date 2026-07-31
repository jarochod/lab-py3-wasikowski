import models


def test_people():
    print("\n🔹 Tworzę użytkownika (User)")
    u = models.User("Ala")

    print("\n🔹 Tworzę pracownika (Employee)")
    e = models.Employee("Bartek")

    print("\n🔹 Tworzę menedżera (Manager)")
    m = models.Manager("Celina")

    print("\n✅ Obiekty utworzone, wypisuję je:")
    print(u)
    print(e)
    print(m)

if __name__ == "__main__":
    test_people()
