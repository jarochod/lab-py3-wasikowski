# R96. Nazwane argumenty funkcji

def showData(string, number):
    print(string + str(number))

showData(string="Liczba: ", number=10) # Liczba: 10 / w nawiasach podaje funkcji argumenty nazwane
showData(number=10, string="Liczba: ") # Liczba: 10 /  w nawiasach podaje funkcji argumenty nazwane
showData("Liczba: ", 10) # Liczba: 10

# Nawane argumenty z wartościami domyślnymi funkcji
def printUser(name, country = "unknown", email = "default@example.com"):
    print("User: "+ name + " from country: " + country + " and email: " + email)

printUser(country= "UK", name= "Ania") # User: Ania from country: UK and email: default@example.com


# Przykład z kursu
def printCar(brand, name = "concept", year = 1960, color = "black"):
    print(brand, name,year, color)


printCar(name = "T", brand = "Ford") # Ford T 1960 black
printCar(name = "T", year = 1920, brand = "Ford") # Ford T 1920 black

