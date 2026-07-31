# R114. Łańcuchy znaków - konwersje z str - zadanie 4

# Zadanie na Number:
# 1) pobierz liczbę całkowitą od użytkownika do zmiennej
#    za pomocą funkcji input, przekaż do niej informację: Podaj liczbę całkowitą.
# 2) Zmień typ wartości z tekstu na liczbę całkowitą 
# 3) Stwórz funkcję calculateSquareArea z parametrem height
#    która zwraca powierzchnią kwadratu.
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą,
#    wynik pokaż w konsoli.
# 5) Pobierz od użytkownika liczbę dziesiętną, pamiętaj o kropce
#    w liczbie. Oblicz powierzchnię kwadratu z tą wartością,
#    pokaż wynik w konsoli zaokrąglony do 2 miejsc po przecinku. 


##################--------------------
print('\n----wariant1 moj-----\n')

def calculateSquareArea(height):
    return height ** 2


userInput = input("Podaj liczbę całkowitą: ")
intNum = int(userInput)
print("Powierzchnia kwadratu: ", calculateSquareArea(intNum))

userInput = input("Podaj liczbę dziesiętną z kropką: ")
floatNum = float(userInput)
print("Powierzchnia kwadratu: ", round(calculateSquareArea(floatNum), 2))


##################--------------------
print('\n----wariant2 kurs-----\n')

userInput = input("Podaj liczbę całkowitą:")
intNum = int(userInput)

def calculateSquareArea(height):
    return height * height

squareArea = calculateSquareArea(intNum)
print("Powierzchnia kwadratu:", squareArea)

decimalStr = input("Podaj liczbę dziesiętną z kropką:")
decimal = float(decimalStr)
squareArea = calculateSquareArea(decimal)

print(squareArea)
print(round(squareArea, 2))








