# R109. Przydatne funkcje do operacji matematycznych - zadanie

# Zadanie - symulacja kosztów podróży 
# W tym zadaniu skorzystasz z funkcji matematycznych i losowych do symulacji kosztów podróży.
# Użyj danych typów, funkcji matematycznych oraz funkcji z modułu random do wyliczenia i 
# przewidzenia kosztów.   
#
# 1) Stwórz zmienną 'distance' z losową wartoscią od 100 do 1000. która 
# oznacza dystans w kilometrach do pokonania. 
# 2) Oblicz spodziewane spalanie na podróż, przyjmująć że na 100 km spali się 7 litrów
# paliwa. Użyj zaokrąglenia w górę. 
# 3) Przyjmij cenę paliwa za litr jako losową wartość zmiennoprzecinkową między 4.5 a 5.5. 
# Zaokrągl cenę do dwóch miejsc po przecinku. 
# 4) Oblicz całkowity koszt paliwa na pordróż.
# 5) Jeśłi koszt paliwa przekracza 400 zł, wyświetl komunikat o wysokich kosztach 
# podróży. W przeciwnym razie, poinformuj o przystępnych kosztach.

import math
import random

distance = random.randint(100, 1000) # 'distance' / losowa wartość od 100 do 1000

fuelConsumptionPer100km = 7
expectedFuelConsumption = math.ceil(distance / 100) * fuelConsumptionPer100km 

fuelPrice = round(random.uniform(4.5, 5.5), 2)

totalCost = round(expectedFuelConsumption * fuelPrice, 2)
print("Koszt:",totalCost)

if totalCost > 400:
    print("Wysokie koszty podrózy:", totalCost)
else:
    print("Akceptowalnee koszty podróży:", totalCost)



