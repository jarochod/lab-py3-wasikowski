# R50. Operatory tożsamości is oraz is not - zadanie

# Zadanie do wykonania
# Wykorzystaj operatory tożsamości (is, is not) do sprawdzenia relacji miedzy obiektami
# 1) Stwórz zmienną 'text' z wartością "Hello" i użyj metody upper()
#    do wyświetlenia wielkich liter. Sprawdź dostępne metody za pomocą dir().
# 2) Stwórz dwie zmienne 'x' i 'y' z wartością 256. Sprawdź, czy x is y.
# 3) Stwórz listę 'listOne' z kilkoma elementami. Skopiuj 'listOne' do 'listTwo'
#    poprzez przypisanie. Sprawdź, czy listOne is listTwo.
# 4) Zmodyfikuj 'listOne' poprzez dodanie nowego elementu. Sprawdź, czy zmiana
#    wpłynęła na 'listTwo'. Użyj if do wyświetlenia komunikatu o zmianie.
# 5) Stwórz nową listę 'listThree' z takimi samymi elementami, co 'listOne'.
#    Sprawdź, czy listOne is listThree i wyświetl odpowiedni komunikat za pomocą if.

#1
text = "Hello"
print(text)
print(text.upper())
print(dir(text))

#2
x,y = 256, 256
print (x is y) # True

#3
listOne = [1,2,3]
listTwo = listOne
print(listOne is listTwo) # True

#4
listOne.append(4);
if listOne is listTwo: # True
    print("Modyfikacja wpłyneła tez na listTwo")

#5
listThree = [1,2,3,4]
if listOne is listThree: # False
    print("Obie listy takiesame")
else:
    print("listOne i listThree to inne obiekty")