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


def calculateHumanYears(dogYears):
    """
    Oblicza wiek psa w ludzkich latach.

    Parametry:
    dogYears (float): Wiek psa w latach.

    Zwraca:
    float: Wiek psa w ludzkich latach.
    """
    if dogYears <= 2:
        return dogYears * 10.5
    else:
        return 21 + (dogYears - 2) * 4

def get_dog_age():
    """
    Pobiera wiek psa od użytkownika i sprawdza, czy jest to liczba dodatnia.

    Zwraca:
    float: Wiek psa.
    """
    while True:
        try:
            age = float(input("Wprowadź wiek psa w latach: "))
            if age < 0:
                print("Wiek nie może być ujemny. Spróbuj ponownie.")
            else:
                return age
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")

def main():
    """
    Główna funkcja programu, która umożliwia wielokrotne obliczanie wieku psa w ludzkich latach.
    """
    while True:
        dogAge = get_dog_age()
        humanYears = calculateHumanYears(dogAge)
        print(f"Wiek psa w ludzkich latach: {humanYears:.2f}")

        again = input("Czy chcesz obliczyć wiek innego psa? (tak/nie): ").strip().lower()
        if again != "tak":
            print("Dziękujemy za skorzystanie z kalkulatora. Do widzenia!")
            break

if __name__ == "__main__":
    main()
