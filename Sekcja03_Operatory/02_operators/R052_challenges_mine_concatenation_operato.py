# R52. Operator konkatenacji - zadanie

# Zadanie do wykonania:
# Wykorzystaj operator konkatenacji do łączenia stringów i list,
# oraz zastosuj prostą instrukcję warunkową if.
# 1) Połącz dwa stringi 'firstName' i 'lastName' w jeden string 'fullName'
#    i wyświetl go. Dodaj między nimi spację.
# 2) Stwórz dwie listy: 'listOne' z liczbami od 1 do 3 i 'listTwo' z liczbami
#    od 4 do 6. Połącz je w jedną listę 'combinedList' i wyświetl.
# 3) Jeśli długość 'combinedList' jest większa od 5, wyświetl "Lista jest długa".
# 4) Do zmiennej 'greeting' dodaj string 'Hello', a do niej 'fullName'.
#    Sprawdź, czy w 'greeting' znajduje się słowo 'Hello'. Jeśli tak,
#    wyświetl pełne powitanie.

#1
firstName = "Adam"
lastName = "Kowalski"
fulName = firstName + " " + lastName
print(fulName) # Adam Kowalski

#2
listOne = [1,2,3]
listTwo = [4,5,6]
combinedList = listOne + listTwo
print(combinedList) # [1, 2, 3, 4, 5, 6]

#3
if len(combinedList) > 5:
    print("Lista 'combinedList' jest długa")

#4
greeting = "Hello " + fulName

if "Hello" in greeting: # True
    print(greeting)