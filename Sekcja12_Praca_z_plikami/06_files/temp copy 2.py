# Ścieżka do pliku
plik = ".\\test_ANSI.txt"

# Odczyt z kodowaniem cp1250
with open(plik, encoding="cp1250") as f:
    tekst = f.read()

# Zamiana na wielkie litery
tekst_duze = tekst.upper()

# Zapis do pliku z powrotem w cp1250
with open(plik, "w", encoding="cp1250") as f:
    f.write(tekst_duze)
