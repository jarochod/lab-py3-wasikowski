# R124. f string

# Formatowanie ciągów tekstowych w Pythonie umożliwia wstawianie wartości 
# zmiennych bezpośrednio do tekstów, co ułatwia tworzenie dynamicznych 
# wiadomości i raportów. Od wersji Python 3.6 dostępna jest wygodna metoda 
# formatowania ciągów znaków znana jako f-string (formatted string literals).

# Podstawy f-string
# Aby użyć f-string, wystarczy poprzedzić ciąg znaków literą f lub F przed 
# otwarciem cudzysłowu. Wewnątrz ciągu znaków, w nawiasach klamrowych {}, 
# można umieszczać wyrażenia, które zostaną zastąpione ich wartościami.


# F-stringi (f"") są obecnie najczęściej rekomendowanym sposobem formatowania tekstu w Pythonie, głównie ze względu na ich czytelność i wydajność. Powinieneś używać ich jak najczęściej, ale z umiarem – istnieją przypadki, gdzie inne metody mogą być bardziej odpowiednie.

# Dlaczego f-stringi są najlepsze?
# Czytelność - łatwo zobaczyć, jakie wartości są wstawiane.
# Wydajność - szybsze niż .format() i % (operacja string interpolation odbywa się na poziomie kompilacji).
# Elastyczność - można w nich używać wyrażeń, funkcji, metod i formatowania liczbowego.

age = 32
print("age:", age) # age: 32
print(f"age: {age}") # age: 32 / f string jest lepszy, bo ze względu na ich czytelność i wydajność.

print(f"Wiek użytkownika {age} lat.") # Wiek użytkownika 32 lat.

pi = 3.141592
print(f"Wartość liczby pi to około {pi:.2f}")  # Wartość liczby pi to około 3.14
# :.2f określa dokładność po przecinku

lista = ["jabłko", "cytryna"]
print(f"Lista owoców: {lista}") # Lista owoców: ['jabłko', 'cytryna']

pesrson = { "name": "Ania", "age": 32}
print(f"User: {pesrson}") # User: {'name': 'Ania', 'age': 32}
print(f"Imię: {pesrson['name']}, wiek: {pesrson['age']}") # Imię: Ania, wiek: 32



# Użycie f-string do dynamicznego wstawienia wartości zmiennych do tekstu
# Wewnątrz nawiasów klamrowych {} można umieszczać zarówno zmienne, jak i wyrażeni
a = 5
b = 10
print(f"Wynik dodawania {a} i {b} to dokładnie: { a + b }")


# Użycie f-string do dynamicznego wstawienia tekstu w zależności od wyniku
# Wykorzystanie wyrażenia warunkowego (if-else) bezpośrednio wewnątrz f-string
score = 75
print(f"Test zakończony {('sukcesem' if score >= 70 else 'porażką')}")


"""
age = 32
print("age:", age)

print(f"Wiek użytkownika {age} lat.")

pi = 3.141592
print(f"Wartość liczby pi to dokładnie {pi:.2f}")

list = ["jabłko", "cytryna"]
print(f"Lista owoców: {list} ")

person = { "name": "Ania", "age": 32 }
print(f"User: {person}, {person['name']}")

a = 5
b = 10
print(f"Wynik dodawania liczb {a} i {b} to dokładnie: {a + b}")

score = 75
print(f"Test zakończony {('sukcesem' if score >= 70 else 'porażką' )}")
"""