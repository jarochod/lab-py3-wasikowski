# R164. Wstęp do interfejsu użytkownika za pomoca Turtle

'''
Turtle to moduł dostępny w Pythonie na podstawie języka Logo, który został stworzony dla dzieci 
aby uatrakcyjnić im naukę programowania. Turtle pozwala tworzyć proste kształty, figury, 
obrazki oraz animacje w oknie aplikacji dzięki czemu jest przyjemnym wstępem do programowania 
graficznego interfejsu użytkownika.

Tytułowy żółw z modułu turtle porusza się po ekranie dzięki udostępnionym funkcjom:
 forward() lub fd() - poruszanie się do przodu zgodnie z kierunkiem żółwia czyli strzałki co utworzy linie na ekranie,
 backward() lub bk() poruszanie do tyłu,
 left() lub lt() skręcenie w lewo np 90,
 right() lub rt() skręcenie w prawo,
 turtle.mainloop() - czeka na interakcję użytkownika, na razie nie pozwala na automatyczne zamknięcie okna.
 t.clear()	Czyści rysunek, ale zostawia żółwia tam, gdzie jest.
 t.reset()	Czyści rysunek i resetuje żółwia do startu.
 time.sleep(sekundy)	Zatrzymuje program na daną liczbę sekund.
'''

import turtle
import time

# Creating Turtle screen
t = turtle.Turtle()

# moving turtle
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.backward(100)


time.sleep(2) # Zatrzymanie programu na 2 sekund


# shorthend versions
t.lt(45) # left(45)
t.fd(50) # forward(50)
t.rt(90) # right(90)
t.bk(100) # backward(100)

time.sleep(5) # Zatrzymanie programu na 5 sekund
t.reset() # Wyczyść ekran i resetuj żółwia

'''
Turtle - kreska i kolor

Funkcja goTo(x,y) w wygodny sposób przesuwa żółwia w układzie współrzędnych, gdzie początkowym 
punktem jest 0,0 na osi x i y w centrum ekranu horyzontalnie i wertykalnie.

pensize(width) - zmienia grubość linii

color() - zmienia color
'''
 
# x to the right
# y is going up
# moving turtle
t.pensize(10) # pen thickness
t.color("red")
t.goto(0, 100) # x, y
t.goto(0, 0)

t.color("green")
t.goto(100, 0)
t.goto(0, 0)

t.color("blue")
t.goto(0, -100)
t.goto(0,0)

t.color("yellow")
t.goto(-100, 0)
t.goto(0,0)

time.sleep(5) # Zatrzymanie programu na 5 sekund
t.reset() # Wyczyść ekran i resetuj żółwia

"""
Turtle - rysowanie w pętl
Stosująć pętle możemy stworzyć bardziej skomplikowane wzory, które namaluje żółw wraz z animacją.
"""



for i in range(20): 
    turtle.width(i) 
    turtle.forward(60 + 20*i)
    turtle.right(90)
 
time.sleep(5) # Zatrzymanie programu na 5 sekund
turtle.reset() # Wyczyść ekran i resetuj żółwia



import turtle
import random

t = turtle.Turtle()

t.forward(100)
t.right(45)
t.fd(50)
t.left(90)
t.backward(50)
t.penup()

t.goto(0,0)
t.pendown()

time.sleep(5) # Zatrzymanie programu na 5 sekund
t.reset() # Wyczyść ekran i resetuj żółwia

for i in range(20):
    t.color( random.choice(["red","yellow","orange","green","blue"]) )
    t.width(i + 1)
    t.fd( 70 + 20 * i)
    t.right(90)

time.sleep(5) # Zatrzymanie programu na 5 sekund
t.clear() # Wyczyść ekran
turtle.mainloop()
