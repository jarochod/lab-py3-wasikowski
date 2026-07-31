# R77. Program kalkulator w terminalu

calc_operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else "Błąd: dzielenie przez zero!",
    "**": lambda x, y: x ** y
}

num = None

while True:
    if num is None:
        try:
            num = int(input("Podaj liczbę startową: "))
        except ValueError:
            print("Błąd: Wprowadź liczbę całkowitą!")
            continue

    operation = input(f"Podaj operację {list(calc_operations.keys())}, lub 'exit'/'reset': ")
    
    if operation == "exit":
        break
    if operation == "reset":
        num = None
        continue
    if operation not in calc_operations:
        print("Błąd: Wprowadzona została nieprawidłowa operacja.")
        continue

    try:
        second_num = int(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Błąd: Wprowadź liczbę całkowitą!")
        continue

    result = calc_operations[operation](num, second_num)
    print(f"Wynik: {num} {operation} {second_num} = {result}")
    
    if isinstance(result, (int, float)):  # Aktualizujemy tylko, jeśli wynik jest liczbą
        num = result
