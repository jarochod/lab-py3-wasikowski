# R113. Łańcuchy znaków - informacje o użytkowniku - zadanie 3
#
# Funkcje String:  
# 1) Napisz funkcję getUserInformation z trzema parametrami:
#    name, surname, job
# 2) W getUserInformation zmień imię i nazwisko na duże litery,
#    zawód na małe, dodatkowo wyczyść te wartości 
#    z białych znaków na ich początku i końcu
# 3) Połącz imię i nazwisko wraz z innym tekstem aby uzyskać tekst np:
#    "imię: ANIA, nazwisko: KOWALSKA, zawód: testerka" 
# 4) Zwróć powstały tekst z funkcji
# 5) Wywołaj funkcję getUserInformation na następujących 
#    danych i pokaż wynik w konsoli:
#    - Ania, Kowalska, Programistka
#    - Daniel, Lis, Administrator


##################--------------------
print('\n----wariant1 moj-----\n')

def getUserInformation(name, surname, job):
    name = name.strip().upper()
    surname = surname.strip().upper()
    job = job.strip().lower()
    return name, surname, job

name, surname, job = getUserInformation("Ania", "Kowalska", "Programistka")
print(f"imię: {name}, nazwisko: {surname}, zawód: {job}")

name, surname, job = getUserInformation("Daniel", "Lis", "administrator")
print(f"imię: {name}, nazwisko: {surname}, zawód: {job}")

##################--------------------
print('\n----wariant2 moj-----\n')

def getUserInformation(name, surname, job):
    name = name.strip().upper()
    surname = surname.strip().upper()
    job = job.strip().lower()
    return name, surname, job

def printUserInformation(name, surname, job):
    name, surname, job = getUserInformation(name, surname, job)
    print(f"imię: {name}, nazwisko: {surname}, zawód: {job}")

printUserInformation("Ania", "Kowalska", "Programistka")
printUserInformation("Daniel", "Lis", "administrator")


##################--------------------
print('\n----wariant3 Chat GPT-----\n')
def getUserInformation(name, surname, job):
    name = name.strip().upper()
    surname = surname.strip().upper()
    job = job.strip().lower()
    return name, surname, job

def formatUserInformation(name, surname, job):
    return f"imię: {name}, nazwisko: {surname}, zawód: {job}"

# Użycie:
user1 = getUserInformation("Ania", "Kowalska", "Programistka")
print(formatUserInformation(*user1))

user2 = getUserInformation("Daniel", "Lis", "administrator")
print(formatUserInformation(*user2))


##################--------------------
print('\n----wariant4 kurs-----\n')

def getUserInformation(name, surname, job):
    name = name.upper().strip()
    surname = surname.strip().upper()
    job = job.strip().lower()

    text = "imię: " + name + ", nazwisko: " + surname + ", zawód: " + job
    return text

userInfo1 = getUserInformation("Ania", "Kowalska", "Programistka")
print(userInfo1)

print(getUserInformation("Daniel", "Lis", "administrator"))

