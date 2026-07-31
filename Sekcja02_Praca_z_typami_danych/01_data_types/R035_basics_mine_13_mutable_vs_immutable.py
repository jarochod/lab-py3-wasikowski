# R35. Mutowalność kontra niemutowalność

# immutable: int, float, bool, str, tuple, frozenset - to jest niemutowalne.
# Jakiekolwiek operacje na wartościach tych typów danych, tworzy nową wartość w pamięci!
# Po zmianie wartości, fukcja id(), pokaże nowy adres w pamięci, dla nowej wartości.


# Każda próba zmiany obiektu niemutowalnego, utworzy nam automatycznie nowy objekt w pamięci. 



# immutable types: int, float, bool, str, tuple, frozenset
# int
a=1
addr1 = id(a)
a+=1 # zwiększenie a o 1
addr2 = id(a)
print(addr1)
print(addr2)
print(addr1 == addr2) # False

# float
f=3.2
addr1 = id(f)
f = f + 2.5 # zwiększenie f o 2.5
addr2 = id(f)
print(addr1)
print(addr2)
print(addr1 == addr2) # False


# str
s="Hello"
addr1 = id(s)
s = s + " world!"
addr2 = id(s)
print(addr1)
print(addr2)
print(addr1 == addr2) # False

# tuple
t= (0,1,2,3)
addr1 = id(t)
t = t + (4, 5)
addr2 = id(t)
print(addr1)
print(addr2)
print(addr1 == addr2) # False


# Obiekty mutowalne mogą być zmieniane z zachowaniem tego samego miejsca w pamięci
# mutable types: list, set, dict

# list
listData = ['a', 'b']
addr1 = id(listData)
listData += ['c','d']
addr2 = id(listData)
print(addr1)
print(addr2)
print(addr1 == addr2) # True

# set 
setData = {5,6}
addr1 = id(setData)
setData.add(7)
addr2 = id(setData)
print(addr1)
print(addr2)
print(addr1 == addr2) # True


# dict 
dictData = {"a":0, "b":1}
addr1 = id(dictData)
dictData["c"]=2
addr2 = id(dictData)
print(addr1)
print(addr2)
print(addr1 == addr2) # True



# immutable: int, float, bool, str, tuple, frozenset
a = 1
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)


# mutable types: list, set, dict
listData = [0,1,2]
addr1 = id(listData)

listData += [3,4,5]
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)