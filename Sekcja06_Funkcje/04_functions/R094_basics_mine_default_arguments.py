# R94. Domyślne argumenty funkcji

# Funkcja printUser
def printUser(name, country = "unknown", email = "default@example.com"):
    print("User "+ name +" from country: " + country + " and email: " + email)

printUser("Adam","Poland","adam@explane.com") # User Adam from country: Poland and email: adam@explane.com
printUser("Ola") # User Ola from country: unknown and email: default@example.com
printUser("Ada","Poland") # User Ada from country: Poland and email: default@example.com

# Funkcja printCar
def printCar(brand, name = "Concept", year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford") # Ford Concept 1960 black
printCar("Ford", "Mustang") # Ford Mustang 1960 black
printCar("Ford", "Mustang", 1970) # Ford Mustang 1970 black
printCar("Ford", "Mustang", 1970, "red") # Ford Mustang 1970 red
