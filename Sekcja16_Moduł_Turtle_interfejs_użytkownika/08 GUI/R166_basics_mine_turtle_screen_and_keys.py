# R166. Turtle – obsługa ekranu i klawiszy

import turtle
import time

# 🐢 Tworzenie żółwia i okna
t = turtle.Turtle()
win = turtle.Screen()

win.title("Application")
win.bgcolor("yellow")
win.setup(width=550, height=550)

# 🚶 Początkowy ruch żółwia
t.forward(100)
print("x:", t.xcor())
print("y:", t.ycor())

# 🎮 Obsługa klawiszy
def keyPressedW():
    print("W clicked")
    t.forward(100)

def keyPressedS():
    print("S clicked")
    t.backward(100)

def keyPressedA():
    print("A clicked")
    t.left(90)

def keyPressedD():
    print("D clicked")
    t.right(90)

# 🎧 Rejestrowanie zdarzeń klawiatury
win.listen()
win.onkey(keyPressedW, "w")
win.onkey(keyPressedS, "s")
win.onkey(keyPressedA, "a")
win.onkey(keyPressedD, "d")

# 🖥️ Ręczna kontrola odświeżania ekranu
win.tracer(0)

# 🔁 Pętla główna (zamiast mainloop)
while True:
    win.update()
    time.sleep(0.1)

win.mainloop()

'''
## ebook / Python+-+PDF.pdf
# Turtle - obsługa ekranu, klawiszy

import turtle, time

# Creating a window screen
tt = turtle.Turtle()
win = turtle.Screen()
win.title("Application") # screen title
win.bgcolor("green") # screen color

# the width and height can be put as user's choice
win.setup(width=600, height=600) # width, height in px

print(turtle.tracer()) # 1 animation on
# switch off drawing animation/updates
win.tracer(1)
tt.goto(-100,0)
tt.goto(-100,100)
tt.goto(0,100)
tt.goto(0,0)
 # since tracer(0) we have update screen 
win.update() # manually to see changes

def keyPressed():
    tt.fd(100)
 # start listening keyboard events
win.onkey(keyPressed, "w")
win.listen()
print( tt.xcor() ) # pos x
print( tt.ycor() ) # pos y

while True:
    # update screen
    win.update() 

win.mainloop()

# turtle.tracer(0) wskazuje, że nasz aplikacja będzie zarządzała kiedy ma być 
# odrysowanie ekranu, dzięki funkcji win.update(). 
# Wyłącza to animacje żółwia.
'''