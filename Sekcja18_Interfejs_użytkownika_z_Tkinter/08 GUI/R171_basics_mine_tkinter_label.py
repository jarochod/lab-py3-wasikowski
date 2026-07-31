# R171. Tkinter - wstęp oraz widget Label

#-- Wykład S1/4

# Tkinter - biblioteka Pythona umożliwiająca tworzenie aplikacji z interfejsem użytkownika 
# (GUI - Graphical User Interface)

import tkinter as tk

# window is instance of tkinter class
window = tk.Tk()
window.title("Application") # app title


label1 = tk.Label(text="Hello World") # make label
label1.pack()  # add label to window 


label2 = tk.Label(
    text="Hello Again",
    foreground="white",
    background="black"
)
label2.pack()

window.mainloop() # mainloop is Tkinter event loop

# Utworzenie okna wymaga powołanie instancji klasy TK czyli Tkinter
# Okno pozwala na zmianę np. tytułu na belce aplikacji
# Etykietę tworzy się na podstawie klasy Label

#-- Wykład S2/4
# Label - etykieta wyświetla tekst w oknie
import tkinter as tk
window = tk.Tk() 
window.title("Application") # app title
label1 = tk.Label( master = window,
    text="Hello World \n Hello Again!",
    foreground="white",  # text color
    background="green",  # background color
    width=20, # width in characters
    height=3, # height in characters
    cursor = "dot", # arrow, dot
    anchor = tk.E, # east - to the right
    font = "Helvetica 16 bold italic underline",
    padx = 5, # extra space to the left and right
    pady = 5, # extra space to top and down 
)
label1.pack() # add to window
window.mainloop()


# Widget Label wyświetla tekst lub obrazek w określonym oknie (master)
#  oraz akceptuje wiele potencjalnych argumentów.

# width i height - to ilość znaków

# Argument anchor przyjmuje wartość:
# NW, N, NE, W, Center, E, SW, S, SE


#  NW        N      NE

#  W      CENTER

#  SW        S      SE


#-- Wykład S3/4
# Label - obrazki w etykiecie
import tkinter as tk
import os 
window = tk.Tk() 
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
logo = tk.PhotoImage(file="img.png")

label1 = tk.Label(
    master = window, 
    text="Hello World \n Hello Again!",
    foreground="black",  # text color 
    width=10, # width in characters
    height=3, # height in characters
    cursor = "dot", # arrow, dot 
    font = "Helvetica 16 bold italic underline" 
)
label1.pack(side="left") # to left part of screen

label2 = tk.Label(
    master = window,
    image=logo,
    width = 300,
    height= 500
 )
label2.pack(side="right") # to right part of screen
window.mainloop()

# Etykieta może być wzbogacona o obrazek, w  takim wypadku argument width i height 
# wskazuje na ilość pikseli.


#-- Wykład S4/4
# Label - obrazki i tekst w tej samej etykiecie

import tkinter as tk
import os 
window = tk.Tk() 
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
logo = tk.PhotoImage(file="img.png")
label1 = tk.Label(
    master = window, 
    text="Hello World", 
    compound = tk.CENTER,
    # compound = tk.LEFT,
    # compound = tk.RIGHT,
    font = "Helvetica 16 bold italic underline",
    image=logo
 )
label1.pack(side="left")

# config() dynamically changes content
label1.config(text="Hello World \n Hello Again!")
window.mainloop()



####################################################
#-- Wykład - ćwiczenia

import tkinter as tk
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

window = tk.Tk()
window.title("Application")
logo = tk.PhotoImage(file="img.png")

label1 = tk.Label(window, 
        text="Hello World!",
        foreground = "white",
        background = "black",
        width = 20,
        height = 3,
        cursor ="dot",
        font = "Times 18 bold italic underline",
        anchor = tk.W,
        padx = 5,
        pady = 5
        )
label1.pack()

label2 = tk.Label(window, text="Hello again!")
label2.pack()

label3 = tk.Label(window,
            text = "Hello World",
            image=logo,
            width=200,
            height=200,
            foreground="red",
            compound=tk.CENTER)
label3.pack()

label3.config(text="Hello World! \n Hello again!")

window.mainloop()
