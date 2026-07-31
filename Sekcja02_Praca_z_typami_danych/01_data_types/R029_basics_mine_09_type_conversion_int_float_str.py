# R29. Konwersje typów - ćwiczenie

floatNum = 23.24234234
intNum = int(floatNum)
print(type(intNum)) # <class 'int'>
print(intNum) # 23

print( int(" 678    ") ) # 678
print( int(99) ) # 99

intNum = 56
float1 = float(intNum)
print(type(float1)) # <class 'float'>
print(float1) # 56.0


str1 = "123.5476786"
float2 = float(str1)
print(type(float2)) # <class 'float'>
print(float2) # 123.5476786
print( float(89.798))


print("Wartość float1: " + str(float1) + " "+ str(78)+" "+str([1,2,3,4]))
print("Wartość float1:", float1, 78, [1,2,3,4])