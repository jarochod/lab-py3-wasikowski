# R133. Atrybuty klasy

# Programowanie obiektowe w Pythonie - definicja klasy - atrybuty czyli zmienne klasy

# Dane wewnątrz obiektu możemy nie tylko odczytać, ale również je zmienić wpisując po kropce
# (dot operator) nazwę zmiennej/atrybutu i następnie po znaku równości nową wartość.
# person1.name = "Kasia" # nadpisanie
# person1.city = "Waw" # dodanie nowej
# 
# Jeżeli nie ma atrybutu to zostanie dodana nowa z odpowiednią wartością do obiektu, czyli dane
# mogą być dodawane dynamicznie! Nie trzeba ich definiować w definicji klasy.

# prostsza wersja

class Person:
    """
    Klasa reprezentująca osobę.
    """
    def __init__(self, name, surname, country, city=None) -> None:
        self.name = name  # Imię osoby
        self.surname = surname  # Nazwisko osoby
        self.country = country  # Kraj zamieszkania
        self.city = city  # Miasto zamieszkania (opcjonalne)

    def get_full_name(self) -> str:
        """
        Zwraca pełne imię i nazwisko osoby.
        """
        return f"{self.name} {self.surname}"
    
    def print_data(self):
        """
        Wyświetla dane osoby.
        """
        print(f"{self.get_full_name()} {self.country}")

# Tworzenie obiektu osoby
person1 = Person("Ola", "Kowalska", "Polska")
print(person1.name)  # Ola - uzyskanie dostępu do zmiennej/atrybutu name
person1.name = "Kasia"  # Nadpisanie wartości imienia
person1.city = "Waw"  # Dodanie nowego atrybutu miasta
print(person1.city)  # Waw - wyświetlenie nowo przypisanego miasta
person1.print_data()  # Kasia Kowalska Polska - wyświetlenie danych osoby


"""
# wersja (zgodna z konwencją PEP8):

from typing import Optional

class Person:
    def __init__(self, name: str, surname: str, country: str, city = None) -> None:
        self.name = name
        self.surname = surname
        self.country = country
        self.city = city

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"
    
    def print_data(self) -> None:
        print(f"{self.get_full_name()} {self.country}")

person1 = Person("Ola", "Kowalska", "Polska")
print(person1.name)  # Ola
person1.name = "Kasia"  # nadpisanie
person1.city = "Waw"  # dodanie nowej
print(person1.city)  # Waw
person1.print_data()  # Kasia Kowalska Polska
"""
print("\nWykład - ćwiczenia\n")

import random

class Student:
    """
    Klasa reprezentująca studenta.
    """
    def __init__(self, name, surname, age, city, school_name=None, field_of_study=None, country=None) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.school_name = school_name  # Nazwa szkoły
        self.field_of_study = field_of_study  # Kierunek studiów
        self.country = country  # Kraj zamieszkania

    def print_info(self):
        """
        Wyświetla informacje o studencie.
        """
        print(f"{self.name} {self.surname}, wiek: {self.age}, miasto: {self.city}, "
              f"szkoła: {self.school_name}, kierunek: {self.field_of_study}")

class School:
    """
    Klasa reprezentująca szkołę.
    """
    def __init__(self, name, city) -> None:
        self.name = name  # Nazwa szkoły
        self.city = city  # Miasto, w którym znajduje się szkoła
        self.students_list = []  # Lista studentów zapisanych do szkoły
        self.fields_of_study = ["IT", "Matematyka", "Robotyka"]  # Dostępne kierunki studiów

    def add_student(self, student):
        """
        Dodaje studenta do szkoły i przypisuje mu losowy kierunek studiów.
        """
        if isinstance(student, Student):
            self.students_list.append(student)
            student.school_name = self.name
            student.field_of_study = random.choice(self.fields_of_study)
    
    def print_school_info(self):
        """
        Wyświetla informacje o szkole oraz jej studentach.
        """
        print(f"Nazwa szkoły: {self.name}, Miasto: {self.city}")
        print("Studenci:")
        for student in self.students_list:
            student.print_info()

# Tworzenie obiektu studenta
student1 = Student("Kasia", "Lis", 20, "Kraków")
student1.school_name = "Tech School 1"
student1.country = "Polska"
student1.print_info()
print(f"Kraj: {student1.country}")

# Tworzenie drugiego studenta
student2 = Student("Adam", "Kowalski", 21, "Warszawa")

# Tworzenie szkoły i dodawanie studentów
school = School("Tech School", "Warszawa")
school.add_student(student1)
school.add_student(student2)

print()  # Pusta linia dla czytelności
school.print_school_info()


"""
import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printSchoolInfo(self):
        print("School name: ", self.name, " City: ", self.city)
        print("Students:")
        for el in self.studentsList:
            el.printInfo()


student1 = Student("Kasia", "Lis", 20, "Krk")
student1.schoolName = "Tech School 1"
student1.country = "Poland"
student1.printInfo()
print(student1.country)

student2 = Student("Adam", "Kowalski", 21, "Waw")

school = School("Tech School", "Waw")
school.addStudent(student1)
school.addStudent(student2)
print("===")
school.printSchoolInfo()
"""