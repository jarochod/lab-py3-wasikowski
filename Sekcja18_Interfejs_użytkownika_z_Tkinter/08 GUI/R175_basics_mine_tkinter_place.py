# R175. Tkinter - metoda place do rozmieszczenia elementu w oknie

####################################################
#-- Wykład s1/1

# Metoda place() - umieszcza elementy dokładnie w wskazanym miejscu

import tkinter as tk
window = tk.Tk()

l1 = tk.Label(window, text="Label 1", bg="white")
l1.place(x=10, y=10)

l2 = tk.Label(window, text="Label 2", bg="yellow")
l2.place(x=100, y=10, height=50, width=80)

entry1=tk.Entry(window)
entry1.place(x=50, y=100)

window.mainloop()

# x, y- położenie na osi x oraz y w pikselach,
# oś x zaczyna się wartością 0 w lewym górnym rogu, dodatnie wartości do prawej strony ekranu 
# os y również, gdzie wartości rosną dodatnimi wartościami w dół ekranu.
# width, height wielkość widgetu w pikselach



####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Label 1", bg="silver")
label1.place(x=0, y= 20, width=50, height=35)

label2 = tk.Label(window, text="Label 2", bg="red")
label2.place(x=70, y= 70, width=90, height=35)

window.mainloop()

####################################################
#-- mine
import tkinter as tk
window = tk.Tk()

l1 = tk.Label(window, text="Label 1", bg="white")
l1.place(x=10, y=10)

l2 = tk.Label(window, text="Label 2", bg="white")
l2.place(x=10, y=60)

entry1=tk.Entry(window)
entry1.place(x=10, y=30)

entry2=tk.Entry(window)
entry2.place(x=10, y=80)

window.mainloop()