# R102. Scope - zadanie

# Pracownicy w liście z zwiększoną pensją
# 1) Stwórz globalną zmienną employees, która jest pustą listą
# 2) Napisz funkcję addEmployee która przyjmuje email i salary, wewnątrz stwórz
#    słownik z tymi samymi parametrami. Następnie dodaj go do globalnej listy
#    employees stosując funkcję append np someList.append(newElement)
# 3) Wywołaj funkcję addEmployee dla trzech dowolnych pracowników
#    o pensjach: 6000, 8000 i 10000, wpisz dowolne maile
# 4) Dodaj funkcję increaseSalary z dwoma argumentami: employees i pctIncrease
#    Jako pierwszy argument będzie przekazywana lista pracowników, a do drugiego
#    wartość podwyżki np. 15  Przejdź po wszystkich pracownikach i zwiększ
#    pensję pracowników o przekazaną wartość procentową pctIncrease
# 5) Zwiększ pensje pracowników z funkcją increaseSalary o 20%, wyświetl 
#    listę w terminalu


emplyees = []

def addEmployee(email, salary):
    e = {
        "email": email,
        "salary": salary
    }
    emplyees.append(e)

addEmployee("ania@test.com", 6000)
addEmployee("adam@test.com", 8000)
addEmployee("kasia@test.com", 10000)

print(emplyees) # [{'email': 'jan@test.com', 'salary': 6000}, {'email': 'agmieszka@test.com', 'salary': 8000}, {'email': 'adam@test.com', 'salary': 10000}]

def increaseSalary(emplyees,pctIncrease):
    increase = pctIncrease * 0.01  
    for e in emplyees:
        e["salary"] *= 1 + increase

# pctIncrease = 20%
increaseSalary(emplyees,20) # [{'email': 'jan@test.com', 'salary': 7200.0}, {'email': 'agmieszka@test.com', 'salary': 9600.0}, {'email': 'adam@test.com', 'salary': 12000.0}]
print(emplyees)









