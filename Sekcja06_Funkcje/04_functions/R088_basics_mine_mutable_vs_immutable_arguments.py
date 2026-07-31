# R88. Przekazanie mutowalnych i niemutowalnych wartości do funkcji

# immutable: int, float, bool, str, frozenset

"""
def modifyStr(strData):
    print( id(strData) )
    strData += "!"
    print( id(strData) )
    print(strData)


string = "Hello"
print( id(string) )
modifyStr(string)
print(string)


# mutable types: list, set, dict
def modifyList(listData):
    print( id(listData) )
    listData = [1,2,3,4,5,6]
    listData.append(10)
    print( id(listData) )
    

listValue = [0,1,2]
print( id(listValue) )

modifyList(listValue)

"""

print("---------------")
# immutable: int, float, bool, str, frozenset


def modifyStr(strData):
    print(id(strData))
    print(strData)
    strData += "!"
    print(id(strData))
    print(strData)



string = "Hello"
print(id(string))

modifyStr(string)


print(id(string))
print(string)


print("---------------")
# mutable types: list, set, dict
print("1-------modifyList1--------")
def modifyList1(listData):
    print(id(listData))
    listData.append(10)
    print(id(listData))


listValue = [1,2,3]
print(id(listValue))
print(listValue) # [1, 2, 3]

modifyList1(listValue)
print(listValue) # [1, 2, 3, 10]
modifyList1(listValue)
print(listValue) # [1, 2, 3, 10, 10]


print("2-------modifyList2--------")
def modifyList2(listData):
    print(id(listData))
    listData = [1,2,3,4,5,6]
    listData.append(10)
    print(id(listData))
    print(listData)


listValue = [1,2,3]
print(id(listValue))
print(listValue) # [1, 2, 3]

modifyList2(listValue) # [1, 2, 3, 4, 5, 6, 10]
print(listValue) # [1, 2, 3]
modifyList2(listValue) # [1, 2, 3, 4, 5, 6, 10]
print(listValue) # [1, 2, 3]
