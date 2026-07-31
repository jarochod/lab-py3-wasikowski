# R164. Wstęp do interfejsu użytkownika za pomocą Turtle

"""
Turtle to moduł graficzny w Pythonie, wzorowany na języku Logo, który umożliwia rysowanie 
poprzez sterowanie tzw. "żółwiem" (ang. turtle) po ekranie. 
Moduł ten doskonale nadaje się do nauki programowania, zwłaszcza dla początkujących.

Najważniejsze funkcje Turtle:

Ruchy:
- forward(x) / fd(x)      – przesuwa żółwia do przodu o x pikseli
- backward(x) / bk(x)     – przesuwa żółwia do tyłu o x pikseli
- left(kąt) / lt(kąt)     – obraca żółwia w lewo o zadany kąt
- right(kąt) / rt(kąt)    – obraca żółwia w prawo o zadany kąt
- goto(x, y)              – przesuwa żółwia do punktu (x, y)
- penup() / pendown()     – podnosi lub opuszcza pisak (rysowanie lub nie)
- reset()                 – czyści ekran i resetuje żółwia do pozycji początkowej
- clear()                 – czyści rysunek, ale nie resetuje pozycji i orientacji
- pensize(grubość)        – ustawia grubość pisaka
- color("nazwa_koloru")   – ustawia kolor linii
- width(grubość)          – alias dla pensize()
- speed(szybkość)         – ustala prędkość rysowania (1–10 lub "fastest")

Inne:
- time.sleep(sek)         – zatrzymuje program na określoną liczbę sekund
- turtle.mainloop()       – utrzymuje okno aplikacji otwarte (na końcu programu)
"""

import turtle
import time
import random

# Tworzymy instancję żółwia
t = turtle.Turtle()

# === Rysowanie podstawowych linii ===
t.forward(100)       # idź do przodu 100 pikseli
t.right(90)          # skręć w prawo 90 stopni
t.forward(50)
t.right(90)
t.backward(100)      # idź do tyłu 100 pikseli

time.sleep(2)        # pauza 2 sekundy

# Skrócone wersje poleceń
t.lt(45)             # skręt w lewo o 45 stopni
t.fd(50)             # do przodu 50 pikseli
t.rt(90)             # skręt w prawo o 90 stopni
t.bk(100)            # do tyłu 100 pikseli

time.sleep(5)
t.reset()            # wyczyść i zresetuj żółwia

# === Rysowanie linii w różnych kierunkach i kolorach ===

# Zmiana grubości pisaka
t.pensize(10)

# Kolor czerwony – do góry
t.color("red")
t.goto(0, 100)
t.goto(0, 0)

# Kolor zielony – w prawo
t.color("green")
t.goto(100, 0)
t.goto(0, 0)

# Kolor niebieski – w dół
t.color("blue")
t.goto(0, -100)
t.goto(0, 0)

# Kolor żółty – w lewo
t.color("yellow")
t.goto(-100, 0)
t.goto(0, 0)

time.sleep(5)
t.reset()

# === Pętla do rysowania wzoru spiralnego ze zmienną grubością linii ===

for i in range(20):
    t.width(i)                    # zmieniaj grubość linii
    t.forward(60 + 20 * i)        # zwiększaj długość linii
    t.right(90)                   # skręć w prawo

time.sleep(5)
t.reset()

# === Rysunek kombinowany z penup(), pendown() ===

t.forward(100)
t.right(45)
t.fd(50)
t.left(90)
t.backward(50)
t.penup()                         # podnieś pisak (nie rysuj)
t.goto(0, 0)                      # wróć do środka
t.pendown()                       # opuść pisak (rysuj)

time.sleep(5)
t.reset()

# === Pętla z losowymi kolorami i grubością linii ===

for i in range(20):
    t.color(random.choice(["red", "yellow", "orange", "green", "blue"]))  # losowy kolor
    t.width(i + 1)                     # grubość pisaka rośnie
    t.fd(70 + 20 * i)                  # długość kreski rośnie
    t.right(90)

time.sleep(5)
t.clear()  # wyczyść ekran

# === Czekamy na interakcję użytkownika (zamknięcie okna) ===
turtle.mainloop()
