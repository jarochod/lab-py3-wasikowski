# R21. Typ Krotki Tuples

data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafał" # TypeError: 'tuple' object does not support item assignment

names = data + ("Rafał",)
print(names) # ('Ala', 'Ola', 'Kasia', 'Rafał')
print(len(names)) # 4 
print(type(names)) # <class 'tuple'>

numbers = 1, 2, 3
print(type(numbers)) # <class 'tuple'>

emptyTuple = ()
print(emptyTuple) # ()
print(type(emptyTuple)) # <class 'tuple'>

print(names[1]) # Ola
print(names[-1]) # Rafał
print(names[1:3]) # ('Ola', 'Kasia')

cars = ( ("dodge", "ford"), ("pointiac"))
print(cars[0][0]) # dodge

if "ford" in cars[0]:
    print("Ford jest w krotce nr 1") # Ford jest w krotce nr 1

del cars
# print(cars) # NameError: name 'cars' is not defined. Did you mean: 'vars'?

# del names[0] # TypeError: 'tuple' object doesn't support item deletion

tupleX3 = names * 3
print(tupleX3) # ('Ala', 'Ola', 'Kasia', 'Rafał', 'Ala', 'Ola', 'Kasia', 'Rafał', 'Ala', 'Ola', 'Kasia', 'Rafał')
print(type(tupleX3)) # <class 'tuple'>