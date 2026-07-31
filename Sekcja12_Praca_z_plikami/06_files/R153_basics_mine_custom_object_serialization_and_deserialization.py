# R153. Serializacja i deserializacja obiektów na bazie zdefiniowanych klas

# Zapis obiektu na bazie  zdefiniowanej klasy z pickle - serializować można dowolne obiekty np na 
# bazie klas naszego programu co upraszcza pracę z danymi.

print("\nWykład")
import os
import pickle

script_dir = os.path.dirname(__file__)

class Person_:
    def __init__(self, name, surname, city) -> None:
        self.name = name
        self.surname = surname
        self.city = city

    def printInfo(self):
        print(f"{self.name} {self.surname} {self.city}")

person1_ = Person_("Adam", "Kot", "Krk")
person2_ = Person_("Ola", "Kowalska", "Waw")

fh = open(script_dir + "/people_.dat", "wb")
pickle.dump(person1_, fh)
pickle.dump(person2_, fh)
fh.close()

fh = open(script_dir + "/people_.dat", "rb")
person1_r = pickle.load(fh)
person2_r = pickle.load(fh)

print()
person1_r.printInfo()
person2_r.printInfo()



print("\nĆwiczenia")

import os
import pickle # do zapisu danych binarnych

scriptDir = os.path.dirname(__file__)

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self):
        return f"{self.name} {self.surname} {self.city}"


person1 = Person("Ola", "Kowalska", "Krk")
person2 = Person("Adam", "Kot", "Waw")
person3 = Person("Kasia", "Kot", "Gd")

people = [ person1, person2, person3 ]

fh = open(scriptDir + "/people.dat", "wb")
pickle.dump(people, fh) 
fh.close()


fh = open(scriptDir + "/people.dat", "rb")
listFromFile = pickle.load(fh)
fh.close()

print(listFromFile)

for person in listFromFile:
    print(person)