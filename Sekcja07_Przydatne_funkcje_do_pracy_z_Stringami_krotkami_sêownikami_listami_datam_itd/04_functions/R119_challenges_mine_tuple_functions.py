# R119. Przydatne funkcje do operacji na krotkach - zadanie

# Zadanie - analiza danych demograficznych
# W tym zadaniu wykorzystasz krotki do przechowywania i analizy
# danych demograficznych. Użyj podstawowych operacji na krotkach
# do manipulacji danymi oraz do wykonania prostych obliczeń.
#
# 1) Stwórz krotkę `population` zawierającą liczbę ludności w milionach
#    dla pięciu wybranych krajów. Np. Polska - 38, Niemcy - 83 itd.
# 2) Dodaj do krotki `population` dane dla kolejnego kraju używając
#    konkatenacji.
# 3) Wyświetl długość krotki `population`, aby sprawdzić ile jest
#    obecnie danych.
# 4) Sprawdź, czy liczba 100 (milionów ludności) znajduje się w krotce
#    `population`.
# 5) Wyświetl liczbę ludności dla trzeciego kraju w krotce.
# 6) Oblicz minimalną i maksymalną liczbę ludności w krotce `population`.
# 7) Jeśli maksymalna liczba ludności w krotce jest większa niż 500 mln,
#    wyświetl komunikat: "Znaleziono kraj o bardzo dużej populacji".
#    W przeciwnym razie, wyświetl: "Wszystkie kraje mają populację poniżej 500 mln".


##################--------------------
print('\n----wariant1 moj-----\n')
# 1)
population = (38, 83, 60, 46, 120)
# 2)
population += (130,)
# 3)
print("Ilość elementów:", len(population))
# 4)
print("Czy jest kraj o populacji 100 mln?", (100 in population))
# 5
print("Ilość populacji trzeciego kraju w krotce:", population[2])
# 6

min_valume = min(population)
max_valume = max(population)

print("Min liczba ludości z krotki:", min_valume)
print("Max liczba ludości z krotki:", max_valume)
# 7
if max_valume > 500:
    print("Znaleziono kraj o bardzo dużej populacji.")
else:
    print("Wszystkie kraje mają populację poniżej 500 mln.")


##################--------------------
print('\n----wariant2 kurs-----\n')

population = (38, 83, 60, 46, 120)

population += (130,)

print("Ilość elementów:", len(population))
print("Czy jest kraj o populacji 100 mln:", 100 in population)
print("Kraj trzeci w kolejnośći:", population[2])

min = min(population)
max = max(population)
print("Min:", min)
print("Max:", max)

if max > 500:
    print("Jest kraj z 500 mln ludności")
else:
    print("Wszystkie kraje nie mają więcej niż 500 mln")

