# R165. Turtle – kształty z wypełnieniem oraz spirograf

"""
# Wymagania:
Python (moduł turtle)
Graficzne środowisko (nie działa w terminalu tekstowym)

# Funkcje użyte:
pensize() / width() - ustawia grubość linii
color() - ustawia kolor linii
fillcolor() - ustawia kolor wypełnienia
begin_fill() / end_fill() - określają obszar do wypełnienia kolorem
circle() - rysuje koło
goto(x, y) -  przesuwa żółwia bez rysowania
penup() / pendown() - podnosi/opuszcza pióro
reset() - czyści ekran i resetuje żółwia
mainloop() - zapobiega automatycznemu zamknięciu okna
"""


import turtle

# 🔷 Żółw nr 1 – kwadrat i trójkąt
t1 = turtle.Turtle()
t1.pensize(10)
t1.color("blue")
t1.fillcolor("red")

# Kwadrat
t1.penup()
t1.goto(-200, 200)
t1.pendown()
t1.begin_fill()
for _ in range(4):
    t1.forward(70)
    t1.right(90)
t1.end_fill()

# Trójkąt
t1.fillcolor("orange")
t1.penup()
t1.goto(-200, -200)
t1.pendown()
t1.begin_fill()
for _ in range(3):
    t1.forward(70)
    t1.right(120)
t1.end_fill()

# 🔷 Żółw nr 2 – koło
t2 = turtle.Turtle()
t2.width(10)
t2.color("blue")
t2.fillcolor("red")

t2.penup()
t2.goto(200, 130)
t2.pendown()
t2.begin_fill()
t2.circle(35)
t2.end_fill()

# 🔄 Czyścimy ekran przed rysowaniem spirografu
t1.reset()
t2.reset()

# 🔷 Żółw nr 3 – spirograf
t3 = turtle.Turtle()
t3.width(3)
t3.color("green")
t3.speed(0)  # maksymalna prędkość

t3.penup()
t3.goto(0, 0)
t3.pendown()

# Rysujemy spirograf (36 kół obróconych co 10 stopni)
for _ in range(36):
    t3.circle(100)
    t3.left(10)

# 🕸️ Nie zamykaj okna automatycznie
turtle.mainloop()
