# R20. List - zadanie

# 1. Stwórz listę data z kolejnymi liczbami: od 0 do 6
# 2. Pokaż w konsoli długość listy, skasuj 2 element
#    i pokaż długość listy ponownie
# 3. Użyj instrukcji warunkowej if z in do sprawdzenia czy
#    liczba 3 jest w liście data, pokaż informację 
#    w konsoli jeśli zachodzi taka sytuacja. Przykład:
#    if 100 in someList:
#       print("100 jest w liście")
# 4. Użyj pętli for aby pokazać wartości w liście.
#    for el in someList:
#       print("element listy z dodaną wartością 2", el + 2)
# 5. Użyj pętli for aby przejść po elementach listy, ale
#    pokaż ich wartości pomnożone przez 2

data = [0,1,2,3,4,5,6]
print("Długość listy:", len(data))
del data[1]
print("Długość listy po skasowaniu elementu:", len(data))

if 3 in data:
    print("wartość 3 jest w liście")

for num in data:
    print(num)


print("Liczby pomnożone x2")
for num in data:
    newNum = num * 2
    print(newNum)



