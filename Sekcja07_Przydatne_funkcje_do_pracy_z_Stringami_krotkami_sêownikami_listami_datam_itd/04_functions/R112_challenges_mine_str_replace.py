# R112. Łańcuchy znaków - czyszczenie tekstu - zadanie 2
#
# Zadanie String replace
# 1) Stwórz funkcję cleanText, która będzie czyścić                 
#    przekazany tekst z określonych słów.
# 2) Użyj funkcję replace do zamiany podanych słów na 
#    wykropkowane, które wielokrotnie może pojawić się
#    w przekazanym łańcuchu. Dla uproszczenia będziesz
#    zamieniać nazwy języków programowania ;)  np.
#    php zmienisz na ***, java na **** itd 
# 3) Zastąp następujące słowa kluczowe:
#    JavaScript, java, php, html, css
# 4) Zwróć wyczyszczony tekst z funkcji cleanText.
# 5) Wywołaj funkcję na następującym lub podobnym tekście:
#   """Programowanie zacząłem z językiem php, następnie
#    poznałem: html i css, ale obecnie skupiam się na
#    JavaScript"""
#    Wynik pokaż w konsoli.

##################--------------------
print('\n----wariant1 moj-----\n')

def cleanText(text):
    replacements = {
        "javascript": "*" * 10,
        "java": "*" * 4,
        "php": "*" * 3,
        "html": "*" * 4,
        "css": "*" * 3
    }

    for word, repalcement in replacements.items():
        text = text.replace(word, repalcement)

    return text


content = """Programowanie zacząłem z językiem php, następnie korzystałem z
html i css, a na koniec poznałem python, java i javascript """

newContent = cleanText(content)

print("Zmodyfikowany tekst:")
print(newContent)


##################--------------------
print('\n----wariant2 Chat GPT-----\n')

def cleanText(text):
    replacements = {
        "javascript": "*" * 10,
        "java": "*" * 4,
        "php": "*" * 3,
        "html": "*" * 4,
        "css": "*" * 3
    }

    total_changes = 0  # Licznik zamian

    for word, replacement in replacements.items():
        count = text.count(word)  # Liczba wystąpień przed zamianą
        text = text.replace(word, replacement)
        total_changes += count  # Dodajemy do licznika zamian

    return text, total_changes  # Zwracamy zmieniony tekst i liczbę zamian

content = """Programowanie zacząłem z językiem php, następnie korzystałem z
html i css, a na koniec poznałem python, java i javascript """

newContent, changes = cleanText(content)  # Odbieramy dwie wartości

print("Zmodyfikowany tekst:")
print(newContent)
print(f"\nLiczba dokonanych zamian: {changes}")



##################--------------------
print('\n----wariant3 kurs-----\n')

def cleanText(text):
    text = text.replace("javascript", "********")
    text = text.replace("java", "*" * 4)
    text = text.replace("php", "*" * 3)
    text = text.replace("html", "*" * 4)
    text = text.replace("css", "*" * 3)
    return text

content = """Programowanie zacząłem z językiem php, następnie korzystałem z
html i css, a na koniec poznałem python, java i javascript """

newContent = cleanText(content)
print(newContent)