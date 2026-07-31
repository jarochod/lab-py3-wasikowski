# 91. Mutowalne argumenty - zadanie 2
#
# Cel: Napisz program, który analizuje wprowadzone temperatury i wykrywa ich średnią,
# najniższą oraz najwyższą wartość. Program powinien prosić użytkownika o wprowadzanie
# temperatur jedna po drugiej, a następnie zwracać raport analizy.
# Komentarze w kodzie będą po polsku, a nazwy zmiennych i funkcji po angielsku.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie serii temperatur, gdzie każda temperatura wprowadzana jest
#    oddzielnie, a zakończenie wprowadzania sygnalizowane jest przez wpisanie 'koniec'.
# 2) Dla każdej wprowadzonej temperatury, dodaj ją do listy temperatur po konwersji na typ float.
# 3) Po zakończeniu wprowadzania danych, wywołaj funkcję analizującą temperatury, która zwraca
#    krotkę zawierającą średnią, maksymalną i minimalną temperaturę z listy.
#    Uwaga aby pobrac wartośc minimalną z listy wykorzystaj funkcję min() do której przekażesz
#    listę wartości liczbowych, tak samo max() oraz sum()
# 4) Wyświetl wyniki analizy użytkownikowi.
#
# Rozwiązanie:

# temperatures = [10,11,12,13,14]

def analizeTemperes(temperatures):
    
    avgTemp = sum(temperatures) / len(temperatures)
    maxTemp = max(temperatures)
    minTemp = min(temperatures)
    
    return (avgTemp ,maxTemp, minTemp)

temperatures = []
while True:
    temp = input("Podaj kolejną tempetarurę lub wpisz 'koniec' aby zakończyć: " )
    if temp.lower() == "koniec":
        break
    else:
        temperatures.append(float(temp))

analizeTemp = analizeTemperes(temperatures)

avg = analizeTemp[0]
min = analizeTemp[1]
max = analizeTemp[2]

print("avg:", analizeTemp[0])
print("min:", analizeTemp[1])
print("max:", analizeTemp[2])

# rozbicie krotki na poszczególne wartości
avgTemp,maxTemp,minTemp = analizeTemp
print("Średnia temperatura:", avgTemp)
print("Maksymalna temperatura:", maxTemp)
print("Minimalna temperatura:", minTemp)
