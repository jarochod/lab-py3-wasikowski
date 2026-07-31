# R26. Typ Set i Frozenset - zbiór

setData = {2,3,1,4,5}
setData.add(22)

setData.discard(1)
print(type(setData)) # <class 'set'>
print(setData) # {2, 3, 4, 5, 22}

for v in setData:
    print(v)

frozenData = frozenset(setData)
print(type(frozenData)) # <class 'frozenset'>
# frozenData.add(56) # błąd! # AttributeError: 'frozenset' object has no attribute 'add'

for value in frozenData:
    print(value)




























"""
setData = { 2,3,1,4,5 }
setData.add(22)

setData.discard(1)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData)
print(type(frozenData))
#frozenData.add(56) # błąd!

for value in frozenData:
    print(value)

"""