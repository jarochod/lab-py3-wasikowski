# R49. Operatory tożsamości is oraz is not

# operatory tożsamości

strData = "test"

print( dir(strData) )

print( strData.upper() ) # TEST

intData = 10
print( dir(intData) )

a = [1,2,3,4,5]
b = a

print( a is b ) # True
a.append(77)
print(a) # [1, 2, 3, 4, 5, 77]
print(b) # [1, 2, 3, 4, 5, 77]

print( a is not b ) # False

c = [3,4,5]
print( a is c ) # False
print( a is not c ) # True
