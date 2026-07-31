# R104. Wyrażenia Lambda

# Wyrazenia lambda są to jednolinijkowe anonimowe funkcje, bez nazwy. Tworzone są za pomocą słowa
# kluczowego lambda po którym następuje lista parametrów. Po dwukropku znajduje się
# własciwy kod funkcji. Funkcję lambda można też przypisać do zmiennej i wywołać jak zwykłą funkcję.

# Poniższa funkcja lambds przyjmuje dwa argumenty a oraz b i zwraca ich sumę, return nie jest potrzebne,
# wynik wyrażenia jest automatycznie zwracany z lambda.

print("\n---Czesc1---")

sum = lambda a, b: a + b

print( sum(10, 5) ) # 15
print( sum(4, 3) ) # 7

# Wyrażenie lambda może być również zwrócone przez zwykłą funkcję, dzięki czemu można ją
# wywołać w razie potrzeb.

# zwrócona jest funkcja lambda, która zapamiętuje wartośc n
def genFunc(n):
    return lambda a: a * n

doubler = genFunc(2) # doubler jest lambda z n o wartości 2
print( doubler(5) ) # 10
print( doubler(7) ) # 14

tripler = genFunc(3)
print( tripler(2) ) # 6
print( tripler(3) ) # 7

# Po co są wyrazenia lambda?
# Wyrażenia lambda przydają się nabardziej w funkcjach wyższego rzędu, czyli takich,
# które jako argument przyjmują inne funkcje lub zwracają funkcję.

# Przykładem jest funkcja r=map(func,seq) przyjmuje funkcję, którą wywoła na wszystkich
# elementach seq, po czym zwróci sekwencję zmodyfikowanych przez func elementów w postaci
# literatora, więc można skonwertować wynik na listę poprzez list()

listData = [1,2,3,4,5]

result = map( lambda x: x *2, listData)
print(result) # <map object at 0x00000202683B6BC0>
print(list(result)) # [2, 4, 6, 8, 10]


print(list(map( lambda x: x*3, listData))) # [3, 6, 9, 12, 15]

# Funkcja filter przyjmuje wyrażenie lambda, które jeśli zwróci true sprawi, że dany 
# emelent listy znajdzie się w wynikowej sekwencji.

listData = ["Ola", "Włodzimierz", "Kasia", "Izydor"]
result = filter(lambda x: len(x) <= 5, listData)
print(result) # <filter object at 0x000001A018E973A0>
print(list(result))

# Funkcja reduce redukuje sekwencję do pojedynczej wartości
# reduce musi zostać zaimportowane

from functools import reduce # import funkcji reduce

numSum = reduce( lambda x, y: x+y, [1, 2, 3, 4, 5])
print("Suma liczb:",numSum)

print("\n---Czesc2---")

from functools import reduce

sum = lambda a,b: a + b

print( sum(4,5) ) # 9
print( sum(14,5) ) # 19


def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2)
print( doubler(4) ) # 8


listData = [0,1,2,3]

result = list( map(lambda a: a * 3, listData ) )
print(result)

result = list( filter(lambda a: a > 1, listData) )
print(result)

result = reduce( lambda x,y: x + " " + y, ("Ola", "Ania") )
print(result)
