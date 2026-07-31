# R164. Wstęp do interfejsu użytkownika za pomoca Turtle

import turtle
import random
import time

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

turtle.mainloop()