# R65. Pętla for

# Pętla for służy do iterowania po sekwencjach, takich jak lista, krotka, słownik, zbiór czy łańcuch znaków.

listData = [1,2,3,4] # iteracja listy
for v in listData:
    print(v)

tupleData = ("one", "two", "three") # iteracja krotki
for v in tupleData:
    print(v)

setData = {3,2,1} # iteracja zbioru
for v in setData:
    print(v)

strData = "Hello" # iteracja Stringa
for v in strData:
    print(v)

# iteracja słownika
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for v in dicttionaryData:
    print(v) # wyświetlanie kluczy słownika

# iteracja słownika, pokazanie wartości
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for v in dicttionaryData:
    print(dicttionaryData[v]) # wyświetlanie wartości słownika

# iteracja słownika, klucz i wartość
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for key, value in dicttionaryData.items():
    print(key,":",value) # klucz i wartość

# iteracja słownika
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for key in dicttionaryData.keys():
    print(key) # wyświetlenie klucza słownika

# iteracja słownika
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for value in dicttionaryData.values():
    print(value) # wyświetlanie wartości słownika


# iteracja słownika
dicttionaryData = { "Ola": "ola@example.com", "Ania": "ania@example.com" }
for value in dicttionaryData.values():
    print(value) # wyświetlanie wartości słownika
else: print("for loo ended") # dodatkowo zastosowanie else

# iteracja listy
for v in [1,2,3,4]:
    print(v*2)

# iteracja krotki
for v in ("Ania", "Ola", "Rafał"):
    print(v)

# iteracja zbioru
for el in {3,4,5,6,"Ola"}:
    print(el)

# iteracja łańcha znaków
for v in "Hello":
    print(v)
else: 
    print("Pętla zakończona")


# iteracja słownika
dicttionaryData = { "Ania" : "ania@example.com", "Adam" : "adam@example.com" }

for key in dicttionaryData:
    print(key) # wyświetlenie klucza słownika

for key in dicttionaryData.keys():
    print(key) # wyświetlenie klucza słownika

for key in dicttionaryData.keys():
    print( dicttionaryData[key] ) # wyświetlenie wartości klucza słownika

for key, value in dicttionaryData.items():
    print(key,":",value) # wyświetlenie klucza i wartości słownika

for value in dicttionaryData.values():
    print(value) # wyświetlenie wartości słownika