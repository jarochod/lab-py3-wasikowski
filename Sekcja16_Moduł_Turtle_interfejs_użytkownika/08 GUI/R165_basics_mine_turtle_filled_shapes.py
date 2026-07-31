# R165. Turtle - kształty z wypełnieniem oraz spirograf

import turtle
t1 = turtle.Turtle() # Tworzymy żółwia

t1.pensize(10) # grubość linii
t1.color("blue") # kolor linii
t1.fillcolor("red") # kolor wypełnienia

t1.penup()
t1.goto(-200,200)
t1.pendown()

#  Kwadrat
t1.begin_fill()
for _ in range(4):
    t1.forward(70)
    t1.right(90)
t1.end_fill()

t1.fillcolor("orange") # kolor wypełnienia
t1.penup()
t1.goto(-200, -200)
t1.pendown()

# Trojkąt
t1.begin_fill()
for _ in range(3):
    t1.forward(70)
    t1.right(120)
t1.end_fill()

# Koło
t2 = turtle.Turtle()
t2.width(10) # grubość linii
t2.color("blue") # kolor linii
t2.fillcolor("red") # kolor wypełnienia


t2.penup()
t2.goto(200, 130)
t2.pendown()
t2.begin_fill()
t2.circle(35)
t2.end_fill()

# Czyścimy ekran przed narysowaniem spirografu
t1.reset()
t2.reset()

#Spirograf
t3 = turtle.Turtle()

t3.width(3) # grubość linii
t3.color("green") # kolor linii

t3.penup()
t3.goto(0, 0)
t3.pendown()
t3.speed(50)

for _ in range(36):
    t3.circle(100)
    t3.left(10)


turtle.mainloop()

"""
import turtle

t1 = turtle.Turtle()
t1.pensize(10)
t1.color("blue")
t1.fillcolor("red")

t1.penup()
t1.goto(-200, 200)
t1.pendown()

t1.begin_fill()
for i in range(4):
    t1.forward(70)
    t1.right(90)
t1.end_fill()


t1.fillcolor("orange")
t1.penup()
t1.goto(-200, -150)
t1.pendown()

t1.begin_fill()
for i in range(3):
    t1.forward(70)
    t1.right(120)
t1.end_fill()


t2 = turtle.Turtle()
t2.width(10)
t2.color("blue")
t2.fillcolor("red")
t2.penup()
t2.goto(200, 150)
t2.pendown()
t2.begin_fill()
t2.circle(50)
t2.end_fill()


t3 = turtle.Turtle()
t3.width(3)
t3.color("green")
t3.penup()
t3.goto(0, 0)
t3.pendown()
t3.speed(50)

for i in range(360):
    t3.circle(100)
    t3.left(10)

turtle.mainloop()
"""