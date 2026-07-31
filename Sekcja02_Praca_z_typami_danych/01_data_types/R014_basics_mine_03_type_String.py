# R14. Typ łańcuch znaków - String - ćwiczenie

str = "Hello World!"
print(str);
print( len(str))
print( type(str))

print( str[len(str)-1])
print( str[0:5] ) # Hello

print( str * 4 ) # Hello World!Hello World!Hello World!Hello World!
strX3 = str * 3
print(strX3) # Hello World!Hello World!Hello World!

str2 = str + " and Hello again!"
print(str2) # Hello World! and Hello again!

print(str2[6:]) # World! and Hello again!

# co 3 literka z łancucha znaków
print(str2[::3]) # HlWl deogn
print(str2[1::3]) # eooda l a!

multiLine = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)

multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia linia\tlinia \" \\ "
print(multiLine2)
