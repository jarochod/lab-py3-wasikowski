# R108. Przydatne funkcje do operacji matematycznych

# Podstawą pracy z danymi jest konwersja między jednym typem, a drugim - np z str na int
string = str(12.56)
print( type(string)) # <class 'str'>

listData = str( [0,1,2,3])
print( type(listData) ) # <class 'str'>

number = int("67")
print( type(number)) # <class 'int'>

number2 = float("20.03")
print( type(number2)) # <class 'float'>

##############

# Przydatne funkcje w pracy z danymi - funkcje matematyczne

import math
# wartość bezwzględna
print( abs(5) ) # 5
print( abs(-5) ) # 5

# zaokrąglenie do najmniejszej liczy całkowitej nie  mniej niż podana wartość 
print( math.ceil(6.78) ) # 7
print( math.ceil(20.12) ) # 20
print( math.ceil(-3.23) ) # -3

# zaokrąglenie do największej liczby całkowitej nie wiekszej niż podana wartość
print( math.floor(6.78) ) # 6
print( math.floor(20.12) ) # 20
print( math.floor(-3.23) ) # -4

# max zwróci największą wartość z przekazanych
print( max(12, 3, 78, 32, 11) ) # 78
print( max( [9, 67, 43, -2] )) # 67

# min zwróci najmniejszą wartość z przekazanych
print( min(12, 3, 78, 32, 11)) # 3
print( min( [8, 67, 43, -2])) # -2

print( pow(2, 3) ) # to samo jak x**y = 8
print( math.sqrt(16) ) # pierwiastek 4.0

# zaokrąglanie do 3 miejsc po przecinku 23.123
print( round(23.12345, 3) ) # 23.123

import random
# losowy float od 0 i mniejszy od 1 np 0.92
print( random.random() )

# losowy element z listy, krotki lub str
print( random.choice([4,3,8])) # np 3
print( random.choice(("Ola", "Ania", "Adam"))) # np Ola

# losowy elemnt z zakresu: start, stop, step
print( random.randrange(0,25,5)) # np 20

# ustawia losowo elementy listy
listData = [0,1,2,3,4]
random.shuffle(listData)
print(listData) # np [0, 4, 3, 1, 2]

# losowy float większy od x i mniejszy  od y
print( random.uniform(2.3, 10.78)) # np 7.348216835414066

# Dodatkwo python oferuje wiele funkcji trygonometrycznych jak acos(), asin(), atn(), cos() itd.


# początek - ćwiczeń
import math
import random

print("\nĆwiczenia")
print("---1---")

print( type( str(12) ) )
print( type( str([12, 34]) ) )

number = int("123")
print( type(number) )

number += 10
print(number) # 133
print( "123" + "10" ) # 12310

floatNum = float("45.67")
print( type(floatNum) )
floatNum = floatNum * 2
print( floatNum ) # 91.34

print("\n---2---")

# abs() - wartośc bezwględna
print( abs(9) )
print( abs(-9.1) )

# math.ceil() - zaokrągla w górę, do liczby całkowitej
print( math.ceil(11.0000001) ) # 12
print( math.ceil(11.9999999) ) # 12
print( math.ceil(-1.0000001) ) # -1
print( math.ceil(-1.999999) ) # -1

# math.floor() - zaokrągla w dół do liczbt całkowitej
print( math.floor(11.0000001)) # 11
print( math.floor(11.9999999) ) # 11
print( math.floor(5.12) ) # 5
print( math.floor(-5.12) ) # -6
print( math.floor(-5.9999999) ) # -6

# max() - zwraca maksymalną wielkość z przekazanych wartości - argumnetów, sekwencji, listy
# min() - zwraca minimalną wielkość z przekazanych wartości - argumnetów, sekwencji, listy
print( max(10,1,-9,33,89,0)) # 89 / zbiór argumentów
print( max( [10,1,-9,33,89,0] )) # 89 / sekwencja
print( max( (10,1,-9,33,89,0) )) # 89 / krotka
print( min(10,1,-9,33,89,0)) # -9 / zbiór argumentów
print( min( [10,1,-9,33,89,0] )) # -9 / sekwencja
print( min( (10,1,-9,33,89,0) )) # -9 / krotka

# pow() - potęgowanie
print(4 ** 3) # 64
print( pow(4, 3)) # 64

# math.sqrt() - pierwiastkowanie
print( math.sqrt(121)) # 11.0

import random

# random.random() zwraca losową liczbę zmiennoprzecinkową z zakresu [0.0, 1.0)
print(random.random())  # np. 0.3046352580038053

# random.random() * 100 zwraca liczbę z zakresu [0, 100)
print(random.random() * 100)  # np. 26.024297433034484

# int(random.random() * 100) zwraca liczbę całkowitą z zakresu 0-99
print(int(random.random() * 100))  # np. 13

# random.choice([]) zwraca losowy element z listy lub krotki
print(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # np. 9
print(random.choice((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))  # np. 9
print(random.choice(("Ola", "Ania", "Adam")))  # np. Ania

# random.randrange(start, stop, step) zwraca losową liczbę z podanego zakresu
print(random.randrange(-10, 30, 5))  # np. 5

# random.shuffle() losowo przetasowuje elementy w liście
listData = [0, 1, 2, 3, 4, 5, 6]  # typ mutowalny
random.shuffle(listData)
print(listData)  # np. [3, 0, 6, 1, 4, 2, 5]


"""
## Część z pliku kursu

import math
import random

print( type( str(12) ) )
print( type( str([12, 34]) ) )

number = int("123")
print( type(number) )

number += 10
print(number) # 133
print( "123" + "10" )

floatNum = float("45.67")
print( type(floatNum) )
floatNum = floatNum * 2
print( floatNum )


print( abs(9) )
print( abs(-9.1) )

print( math.ceil(11.00000001) ) # 12
print( math.ceil(9.999999) ) # 10
print( math.ceil(-1.000000001) ) # -1
print( math.ceil(-1.999999) ) # -1

print( math.floor(11.00000001) ) # 11
print( math.floor(11.99999999999) ) # 11
print( math.floor(5.12) ) # 5
print( math.floor(-5.12) ) # -6
print( math.floor(-5.999999999) ) # -6


print( max(10,1,-9,33,89,0) ) # 89
print( max( [10,1,-9,33,89,0]) ) # 89
print( max( (10,1,-9,33,89,0) ) ) # 89
print( min( (10,1,-9,33,89,0) ) ) # -9
print( min( [10,1,-9,33,89,0] ) ) # -9
print( min( 10,1,-9,33,89,0 ) ) # -9

print( 4 ** 3 ) # 64
print( pow(4, 3) ) # 64

print( math.sqrt(128) ) # 11.31...

print( round(12.7891234, 3) )
print( round(12.7891234, 2) )
print( round(12.7891234, 1) )


print( random.random() ) 
print( random.random() * 100 ) 
print( int(random.random() * 100) ) 

print( random.choice([0,1,2,3,4]) )
print( random.choice( ("Ola", "Ania", "Adam") ) )

print( random.randrange(-10, 30, 5) )

listData = [0,1,2,3,4,5,6]
random.shuffle(listData)

print(listData)

"""

