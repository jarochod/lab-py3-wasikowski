# R120. Przydatne funkcje do operacji na słownikach

##################--------------------
print('\n----wykład-----\n')

# Praca z słownikami

data = { "name": "Kasia", "city": "Waw"}

print( data["name"]) # pobranie elementu z key name, Kasia
data["name"] = "Ola" # modyfikacja elementu
print(data) # {'name': 'Ola', 'city': 'Waw'}

emailKey = "email"
data[emailKey] = "ola@example.com"
print(data) # {'name': 'Ola', 'city': 'Waw', 'email': 'ola@example.com'}

del data["city"] # skasowanie elementu
print(data) # {'name': 'Ola', 'email': 'ola@example.com'}

data.clear() # skasowanie wszystkich elementów
print(data) # {}

data = { "name": "Kasia", "city": "Waw"}
print( len(data) ) # 2 / długość słownika

copy = data.copy() # tworzy płytką kopię słownika
print( copy ) # {'name': 'Kasia', 'city': 'Waw'}

# tworzy słownik z podanymi kluczami, wartościami jako None
data = {}
print(data.fromkeys(("name", "email", "country"))) # {'name': None, 'email': None, 'country': None}

# zwraca istniejącą wartość klucza lub drugi argument
print( data.get("postal code", "DEFAULT") ) # DEFAULT

print( "name" in data) # True / czy klucz jest w słowniku

print( data.keys() ) # dict_keys(['name', 'city', 'code']) / zwraca listę kluczy
print( data.values() ) # dict_values([None, None, None]) / zwraca listę wartości

##################--------------------
print('\n----wykład - ćwiczenia-----\n')

data = { "name" : "Ola", "city" : "Waw" }
print( data["name"] ) # Ola
dataPostalCode = "postalCode"
data[dataPostalCode] = 12345 # dodanie elemetu poprzez odwołanie się do elementu
print( data ) # {'name': 'Ola', 'city': 'Waw', 'postalCode': 12345}
print( len(data) ) # 3 / długość słownika

del data["city"] # kasowanie elementu
print(data) # {'name': 'Ola', 'postalCode': 12345}

data.clear() # kasowanie przystkich elementów
print(data) # {}

data = { "name": "Kasia", "city": "Krk"}
dataCopy = data.copy()
print(dataCopy) # {'name': 'Kasia', 'city': 'Krk'}
print( data["name"] is dataCopy["name"]) # True / data["name"] i dataCopy["name"] ma ten sam obiekt w pamięci
print( data is dataCopy ) # False / data i dataCopy to dwa różne obiekty w pamięci

data2 = dict.fromkeys( ["name", "city", "code"] ) # nowy słownik z kluczami "name", "city" i "code", ale wszystkim kluczom przypisuje domyślną wartość None
print( data2 ) # {'name': None, 'city': None, 'code': None}
data2 = dict.fromkeys( ("name", "city", "code") ) # nowy słownik z kluczami "name", "city" i "code", ale wszystkim kluczom przypisuje domyślną wartość None
print( data2 ) # {'name': None, 'city': None, 'code': None}

data3 = dict.fromkeys( ("name", "city", "code"), 0 ) # nowy słownik z kluczami "name", "city" i "code", ale wszystkim kluczom przypisuje domyślną wartość 0
print( data3 ) # {'name': 0, 'city': 0, 'code': 0}

print( data2.get("x", "DEFAULT") ) # DEFAULT / data2 nie ma klucza "x", więc metoda zwraca "DEFAULT" zamiast zgłosić błąd KeyError

print( "name" in data2 ) # True / sprawdzenie czy dany klucz "name" istnieje w słowniku data2

print( data2.keys() ) # dict_keys(['name', 'city', 'code']) / metoda pozwala uzyskać klucze słownika.
print( data2.values() ) # dict_values([None, None, None]) / metoda pozwala uzyskać wartości słownika.

