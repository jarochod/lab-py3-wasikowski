# R32. type conversion tuple list dict set frozenset - zadanie do wykonania

# Zadanie do wykonania:
# 1. Stwórz listę 'numbers' zawierającą liczby od 7 do 12.
#    Wyświetl tę listę.
# 2. Zamień listę 'numbers' na krotkę 'tupleNumbers' i
#    wyświetl wynik.
# 3. Utwórz listę 'mixedList' składającą się z różnych typów
#    danych, np. string, liczba całkowita, liczba zmiennoprzecinkowa.
#    Wyświetl 'mixedList'.
# 4. Przekształć 'mixedList' w zbiór 'setMixed' i wyświetl jego
#    typ oraz zawartość.
# 5. Zamień 'tupleNumbers' na zamrożony zbiór 'frozenSetNumbers'
#    i wyświetl jego typ oraz zawartość.
# 6. Stwórz krotkę 'nameAgePairs' zawierającą pary (imię, wiek),
#    a następnie na jej podstawie utwórz słownik 'ageDict'.
#    Wyświetl słownik, a potem wyświetl wiek osoby o imieniu 'Marek'.


print("1----------")
numbers = [7,8,9,10,11,12]
print(type(numbers)) # <class 'list'> lista
print(numbers) # [7, 8, 9, 10, 11, 12]

print("2----------")
tupleNumbers = tuple(numbers)
print(type(tupleNumbers)) # <class 'tuple'> krotka
print(tupleNumbers) # (7, 8, 9, 10, 11, 12)

print("3----------")
mixedList = ["Marek", 12, 14.12]
print(type(mixedList)) # <class 'list'> lista
print(mixedList) # ['Marek', 12, 14.12]


print("4----------")
setMixed = set(mixedList)
print(type(setMixed)) # <class 'set'> zbiór
print(setMixed) # {'Marek', 12, 14.12}

print("5----------")
frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers)) # <class 'frozenset'> zamrożnony zbiór
print(frozenSetNumbers) # frozenset({7, 8, 9, 10, 11, 12})

print("6----------")
nameAgePairs = (("Marek", 18),("Ala", 25),("Jan", 30))
ageDict=dict(nameAgePairs)
print(type(ageDict)) # <class 'dict'> słownik
print(ageDict) # {'Marek': 18, 'Ala': 25, 'Jan': 30}

print("Wiek osoby o imieniu \'Marek\':", ageDict["Marek"]) # Wiek osoby o imieniu 'Marek': 18