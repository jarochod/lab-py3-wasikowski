# R166. Turtle – obsługa ekranu i klawiszy

"""
🎯 Cel lekcji:
Nauczyć się, jak:
konfigurować okno turtle.Screen()
przypisywać funkcje do klawiszy (onkey)
poruszać żółwiem za pomocą klawiatury
używać win.tracer() i win.update() do ręcznego odświeżania
"""


"""
💡 Co robi ten kod:
turtle.Screen()     Tworzy okno graficzne
win.setup(...)      Ustawia rozmiar okna
t.xcor() / t.ycor() Zwracają aktualne współrzędne żółwia
t.forward()         Przesuwa żółwia do przodu
t.backward()        Przesuwa żółwia do tyłu
t.left() / t.right() Obraca żółwia w lewo/prawo o podany kąt
win.onkey(...)      Przypisuje funkcje do klawiszy
win.listen()        Uruchamia nasłuchiwanie klawiatury
win.tracer(0)       Wyłącza automatyczne odświeżanie ekranu
win.update()        Ręcznie odświeża ekran
win.bye()           Zamyka okno turtle (kończy program)
time.sleep(0.1)     Wprowadza krótki czas pomiędzy klatkami
"""


import turtle
import time

# 🐢 Tworzenie żółwia i okna
t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

# Wyświetlenie początkowych współrzędnych żółwia
print("x:", t.xcor())
print("y:", t.ycor())

# 🎮 Funkcje obsługujące klawisze
def key_pressed_w():
    print("W clicked")
    t.forward(10)

def key_pressed_s():
    print("S clicked")
    t.backward(10)

def key_pressed_a():
    print("A clicked")
    t.left(90)

def key_pressed_d():
    print("D clicked")
    t.right(90)

def key_pressed_esc():
    print("Zamykanie aplikacji...")
    win.bye()

# 🔁 Rejestrowanie klawiszy
win.listen()
win.onkey(key_pressed_w, "w")
win.onkey(key_pressed_s, "s")
win.onkey(key_pressed_a, "a")
win.onkey(key_pressed_d, "d")
win.onkey(key_pressed_esc, "Escape")

# 🖥️ Ręczna kontrola odświeżania ekranu
win.tracer(0)

# 🔁 Pętla główna (zamiast mainloop)
while True:
    win.update()
    time.sleep(0.1)

