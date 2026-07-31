# R110. Przydatne funkcje do operacji na łańcuchach znaków

# Praca na łancuchach znaków

print( "Hello " + "World!" ) # konketenacja Hello World!

print( "Hello" * 2 ) # powtarzanie HelloHello

string = "Hello"
print( string[1] ) # e
print( string[1:3] ) # zakres: el
print( "o" in string ) # True
print( "X" not in string ) # True

mutiLine = """ line 1
line 2
""" # tekst w wielu liniach

print( "some text".capitalize() ) # Some text
print( "ok ok ok".count("ok")) # zlicza ilość ok: 3

# wycentrowanie tekstu do 10 znaków z *
print( "test".center(10, "*")) # ***test***

# wyszukuje łańcuch, gdy znajdzie daje True
print( "Hello world".endswith("world") ) # True
print( "Hello World".startswith("Hel")) # True

# startswith() sprawdza, czy dany ciąg znaków (string) zaczyna się od określonego prefiksu.
# string.startswith(prefix, start, end)
print("Hello World".startswith("Hel"))  # True
print("Hello World".startswith("World"))  # False
print("Hello World".startswith("Wor", 6))  # True (sprawdza od indeksu 6)

# wyszukuje łańcuch, -1 jeśli nie ma lub pozycja w str
print( "Ala ma konta".find("ma") ) # 4 / ma jest pod 4-tym znakiem
print( "Ala ma kota".find("test") ) # -1 bo nie ma
# rfind() wyszukuje od końca
print( "Ola ma psa, Ola ma kota".rfind("Ola") ) # 12


# likwiduje białe znaki od lewej
print("\n \t  Test ".lstrip() ) # "Test "
# likwiduje białe znaki od prawej
print(" Test \n \t ".rstrip() ) # " Test"
# kasuje białe znaki po obu stronach
print("\n \t Test \n \t ".strip() ) # "Test"

# zamienia wystąpienie w łancuchu na inny
# Kasia ma kota, Kasia ma psa.                                                  
print( "Ola ma kota, Ola ma psa.".replace("Ola", "Kasia") ) 

print( "1256346".isalnum() ) # True, łańcych jest liczbą całkowitą
print( "1256346".isalpha() ) # False
print( "Test".isalpha() ) # True, łańcych z znakami alfabetu
print( "Tesst 2".isalpha() ) # False, bo liczba

print( "test".islower() ) # True, bo małe litery
print( " \t ".isspace() ) # True, bo tylko białe znaki
print( "HELLO".isupper() ) # True, bo tylko wielkie litery

# łączy łańcychy w jeden string z separatorem
print( "-".join( ["Ola", "Ania"] ) ) # Ola-Ania

print( len("str lenght") ) # 10
print( "HELLO World".lower() ) # hello world
print( "HELLO World".upper() ) # HELLO WORLD
print( "HELLO World".swapcase() ) # hello wORLD

print("---czesc 2---")

print("Hello " + "World") # Hello Worls
print("Hello" * 3 ) # HelloHelloHello

string = "Hello World!"
print( string[0]) # H
print( string[0:5]) # Hello

print( "Hello" in string ) # True
print( "Hello" not in string ) # False

multiline = """ line 1
line 2
line 3
"""

print( "ala".capitalize() ) # Ala
print( "Ola ma kota, Ola ma psa".count("Ola") ) # 2

print( "Hello".center(20, "-") ) # 2 -------Hello--------

print( string.startswith("Hello") )
print( string.endswith("World!") )

print( string.find("Ola") ) # -1
print( string.find("World") ) # 6
print( "Ola ma psa, Ola ma kota".rfind("Ola") ) # 12

print( "2342345234".isalnum() ) # True
print( "2342345234.".isalnum() ) # False
print( "2342345234 k".isalnum() ) # False
print( "2342345234 k".isalpha() ) # False

print( " kot".isalpha() ) # False
print( "kot".isalpha() ) # True
print( "kot2".isalpha() ) # False

print( "test".islower() ) # True
print( "tesT".islower() ) # False
print( "TEST".isupper() ) # True

print( " \n\n\t ".isspace() ) # True

print( "-|".join( ["Ala","Ola","Adam"] )) # Ala-|Ola-|Adam

print( "Hello World".lower() ) # hello world
print( "Hello World".upper() ) # HELLO WORLD
print( "Hello World".swapcase() ) # hELLO wORLD

print( "  \n \t Hello World \n\n \t ".lstrip() ) # po lewej stronie likwiduje białe znaki
print( "  \n \t Hello World \n\n \t ".rstrip() ) # po prawej stronie likwiduje białe znaki
print( "  \n \t Hello World \n\n \t ".strip() ) # Hello World / po lewej i prawej likwiduje białe znaki

print( "Ola ma psa, Ola ma kota".replace("Ola", "Kasia") ) # Kasia ma psa, Kasia ma kota

# Formatowanie danych
print( "My name is {myName}, I'm from {country}".format(myName = "Kuba", country= "Poland") ) # # My name is Kuba, I'm from Poland
print( "My name is {myName}, my postal code is {code}".format(myName = "Kuba", code= 11798) ) # My name is Kuba, my postal code is 11798
print( "My name is {0}, my postal code is {1}".format("Kuba", 11798) ) # My name is Kuba, my postal code is 11798
print( "My name is {}, my postal code is {}".format("Kuba", 11798) ) # My name is Kuba, my postal code is 11798


##################--------------------
print('\n----wykład ćwiczenia-----\n')

print( "Hello " + "World!" )
print( "Hello" * 3 )

string = "Hello World!"
print( string[0] ) # H
print( string[0:5] ) # Hello

print( "Hello" in string ) # True
print( "Hello" not in string ) # False

# multline = """line 1
# line 2
# line 3
# """

print( "ala".capitalize() )
print( "Ola ma kota, Ola ma psa.".count("Ola") )

print( "Hello".center(20, "-") )

print( string.startswith("Hello") )
print( string.endswith("World!") )


print( string.find("Ola") )
print( string.find("World") )
print( "Ola ma psa, Ola ma kota".rfind("Ola") ) # 12

print( "2342345234".isalnum() )
print( "2342345234.".isalnum() )
print( "2342345234 k".isalnum() )

print( "2342345234 k".isalpha() )
print( " kot".isalpha() )
print( "kot".isalpha() )
print( "kot2".isalpha() )

print( "test".islower() )
print( "tesT".islower() )
print( "TEST".isupper() )

print( "   \n\n\t ".isspace() )

print( "-|".join( ["Ala","Ola","Adam"] ) )

print( "Hello World".lower() )
print( "Hello World".upper() )
print( "Hello World".swapcase() )

print( "   \n \t Hello World \n\n \t ".lstrip() ) 
print( "   \n \t Hello World \n\n \t ".rstrip() ) 
print( "   \n \t Hello   World \n\n \t ".strip() ) 


print( "Ola ma psa, Ola ma kota".replace("Ola", "Kasia") )

print( "My name is {myName}, I'm from {country}".format(myName = "Kuba", country = "Poland") )
print( "My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = 11798) )
print( "My name is {0}, my postal code is {1}".format("Kuba", 11798) )
print( "My name is {}, my postal code is {}".format("Kuba", 11798) )