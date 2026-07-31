# R55. Instrukcja if elif else i wcięcia - zadanie

# Zadanie do wykonania:
# Wykorzystaj instrukcje warunkowe do stworzenia prostego programu
# decyzyjnego, analizując wartość zmiennej 'number'.
# 1) Stwórz zmienną 'number' i przypisz jej wartość 15.
# 2) Sprawdź, czy 'number' jest większe od 10. Jeśli tak, wyświetl komunikat.
# 3) Sprawdź, czy 'number' jest równe 15. Jeśli tak, wyświetl komunikat.
# 4) Użyj `elif` do sprawdzenia, czy 'number' jest równe 20, 25, lub większe od 30.
#    Dla każdego przypadku wyświetl odpowiedni komunikat.
# 5) Jeśli żaden z powyższych warunków nie jest spełniony, użyj `else` do wyświetlenia
#    domyślnego komunikatu.
# 6) Dodaj zagnieżdżoną instrukcję warunkową, aby sprawdzić dodatkowy warunek
#    dla jednego z przypadków.


number = 15
if number > 10: # True
    print("number jest większe od 10")

if number == 15: # True
    print("number jest równy 15")
elif number == 20:
    print("number jest równe 20")
elif number == 25:
    print("number jest równe 25")
elif number > 30:
    print("number jest większe od 30")
else:
    print("inny przypadek")


if number > 10: # True
    print("number jest większe od 10")
    if number % 3 == 0: # True
        print("number jest podzielne przez 3")