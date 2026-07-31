# Utworzenie pliku wejściowego z kodowaniem UTF-8
with open("example.txt", "w", encoding="utf-8") as fh:
    fh.write("Ala ma kota\nKot ma Ale")

# ==== Tryb 'r+' ====
with open("example.txt", "r+", encoding="utf-8") as fh:
    lines = fh.readlines()  # wczytaj wszystkie linie
    
    # Zmień tylko pierwszą linię
    lines[0] = "Pies ma budę\n"
    
    # Przesuń wskaźnik na początek i zapisz wszystkie linie
    fh.seek(0)
    fh.writelines(lines)
    # fh.truncate()  # usuń pozostałości jeśli nowe linie są krótsze

# Pokaż zawartość po trybie 'r+'
with open("example.txt", "r", encoding="utf-8") as fh:
    print("Zawartość po zapisie w trybie 'r+':")
    print(fh.read())

# ==== Tryb 'w+' ====
print("\n==== Tryb 'w+' ====")
with open("example.txt", "w+", encoding="utf-8") as fh:
    fh.write("Nowy początek")
    fh.seek(0)
    print("Zawartość po zapisie w trybie 'w+':")
    print(fh.read())

# ==== Tryb 'a+' ====
print("\n==== Tryb 'a+' ====")
with open("example.txt", "a+", encoding="utf-8") as fh:
    fh.write("\nDopisuję drugą linię")
    fh.seek(0)
    print("Zawartość po dopisaniu w trybie 'a+':")
    print(fh.read())
