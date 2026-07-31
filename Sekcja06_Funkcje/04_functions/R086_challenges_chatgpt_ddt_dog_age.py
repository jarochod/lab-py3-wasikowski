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


# Testowanie sterowane danymi (Data-Driven Testing) DDT
# wykorzystujemy zestawy testowe (test_values i test_again_values) do sprawdzenia różnych przypadków.

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

def test_program():
    test_values = [1, 2, 3, 5, -1, "abc"]
    for dog_age in test_values:
        print(f"Testuję wartość: {dog_age}")
        try:
            dog_age = float(dog_age)
            if dog_age < 0:
                print("Wiek nie może być ujemny. Spróbuj ponownie.")
                continue
            human_years = calculate_human_years(dog_age)
            print("Wiek psa w ludzkich latach:", human_years)
        except ValueError:
            print("Niepoprawna wartość. Wprowadź liczbę.")
            continue

def test_loop():
    test_again_values = ["tak", 12, "niewiem", "nie"]
    for response in test_again_values:
        print(f"Testuję ponowną decyzję: {response}")
        if isinstance(response, str) and response.lower() == "tak":
            print("Ponowne działanie programu...")
        elif isinstance(response, str) and response.lower() == "nie":
            print("Koniec działania programu.")
            break
        else:
            print("Nie rozpoznaje decyzji. Czy chcesz obliczyć wiek innego psa? (tak/nie)")

test_program()
test_loop()
