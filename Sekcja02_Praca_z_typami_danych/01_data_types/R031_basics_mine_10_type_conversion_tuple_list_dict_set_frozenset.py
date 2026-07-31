# R31. Konwersje typów funkcje tuple list dict set frozenset

listData = [1,2,3,4,5,6]
print(type(listData)) # <class 'list'> lista
print(listData) # [1, 2, 3, 4, 5, 6]
tupleData = tuple(listData)
print(type(tupleData)) # <class 'tuple'> krotka
print(tupleData) # (1, 2, 3, 4, 5, 6)

print("------")

otherList = list(("Ola", 23, 234))
print(type(otherList)) # <class 'list'> lista
print(otherList) # ['Ola', 23, 234]

print("------")

setData = set(otherList)
print(type(setData)) # <class 'set'> zbiór
print(setData) # {'Ola', 234, 23}

print("------")

frozensetData = frozenset(tupleData)
print(type(frozensetData)) # <class 'frozenset'> zamrożony zbiór
print(frozensetData) # frozenset({1, 2, 3, 4, 5, 6})

print("------")

tupleData = ( ("Ola", 1234), ("Adam", 23654) )

dictData = dict(tupleData)
print(type(dictData)) # <class 'dict'> słownik
print(dictData) # {'Ola': 1234, 'Adam': 23654}
print(dictData["Ola"]) # 1234