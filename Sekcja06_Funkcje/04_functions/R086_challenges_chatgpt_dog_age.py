# R86. return - zadanie

# Zadanie: Kalkulator wieku psa w ludzkich latach
#
# Cel: Napisz program, który przelicza wiek psa na ludzkie lata. Program powinien prosić użytkownika
# o wprowadzenie wieku psa, a następnie obliczyć i wyświetlić jego wiek w ludzkich latach.
# Pierwsze dwa lata życia psa liczymy jako 10.5 ludzkiego roku za każdy, a każdy kolejny 
# rok jako 4 ludzkie lata.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculateHumanYears, która przyjmuje wiek psa jako parametr.
#    W funkcji użyj instrukcji if-elif-else do obliczenia wieku psa w ludzkich latach.
#    Dla uproszczenia załóżmy że ilość lat mniejsza równa 2 musi być pomnożona przez 10.5,
#    a dla większych wartości od 2 trzeba zastosować działanie  21 + (dogYears - 2) * 4
# 2) Użyj pętli, aby umożliwić użytkownikowi wielokrotne używanie kalkulatora bez 
#    restartowania programu.
# 3) Poproś użytkownika o wprowadzenie wieku psa.
# 4) Wywołaj funkcję calculateHumanYears i przekaż jej wiek psa wprowadzony przez użytkownika.
# 5) Wyświetl obliczony wiek psa w ludzkich latach.
#


# Ogólne działanie programu
# 1. Funkcja calculate_human_years(dog_years)
# - Oblicza wiek psa w ludzkich latach zgodnie z zasadą:
# -Przez pierwsze dwa lata życia psa każdy rok odpowiada 10,5 latom ludzkim.
# -Każdy kolejny rok liczy się jako 4 lata ludzkie.
# -Wartość zwracana przez funkcję to wiek psa przeliczony na lata ludzkie.

# 2. Pętla główna (while True)
# - Pobiera od użytkownika wiek psa w latach.
# - Obsługuje błędy związane z wprowadzaniem danych.
# - Po obliczeniu wieku psa w ludzkich latach pyta użytkownika, czy chce kontynuować.
# - Program działa w pętli, dopóki użytkownik nie zdecyduje się zakończyć.


def calculate_human_years(dog_years):
    """
    Oblicza wiek psa w ludzkich latach.
    - Przez pierwsze dwa lata, każdy rok psa liczy się jako 10,5 lat ludzkich.
    - Każdy kolejny rok liczy się jako 4 lata ludzkie.
    
    Parametry:
        dog_years (float): Wiek psa w latach.
    
    Zwraca:
        float: Wiek psa w przeliczeniu na lata ludzkie.
    """
    if dog_years <= 2:
        return dog_years * 10.5
    else:
        return 21 + (dog_years - 2) * 4

while True:
    try:
        dog_age = float(input("Wprowadź wiek psa w latach: "))
        if dog_age < 0:
            print("Wiek nie może być ujemny. Spróbuj ponownie.")
            continue
        human_years = calculate_human_years(dog_age)
        print("Wiek psa w ludzkich latach:", human_years)
    except ValueError:
        print("Niepoprawna wartość. Wprowadź liczbę.")
        continue
    
    while True:
        again = input("Czy chcesz obliczyć wiek innego psa? (wpisz 'tak' lub 'nie'): ").strip().lower()
        if again == "tak":
            break
        elif again == "nie":
            print("Koniec działania.")
            break
        else:
            print("Nie rozpoznaję decyzji. Wpisz 'tak' lub 'nie'.")
    if again == "nie":
        break   