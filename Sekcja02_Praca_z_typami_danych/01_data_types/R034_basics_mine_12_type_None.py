# R34. Typ None

# Typ None
# Oznacza brak wartości np że zmienna nie posiada przypisanej wartości,
# coś jak null w innych językach programowania


data = None
print(type(data)) # <class 'NoneType'>

if data is True:
    print("Data is true")
elif data is False:
    print("Data is False")
else:
    print("Data is None")


# Przykład zastosowania nwartosci i typu None
# currentTaskNumber mówi o tym jaki identyfikator zadania jest przypisany do realizacji użytkownikowi
currentTaskNumber = 10 # użytkownik ma przypisanego zadania o id 10

# jesli currentTaskNumber = None, oznacza to, że użytkownik nie ma przypisanego zadania do realizacji
currentTaskNumber = None # użytkownik nie ma przypisanego zadania

currentTaskNumber = 14 # użytkownik ma przypisanego zadania o id 14
