# R181. Tkinter - Scale - suwak

####################################################
#-- Wykład s1/1

# Widget slider pozwala na wybranie wartośći od from_ do to za pomocą wygodnego suwaka.
# Argument orient ma wartości tk.VERTICAL lub tk.HORIZONTAL

# 1. aktualizacja tylko po kliknięciu przycisku

import tkinter as tk
window = tk.Tk()
def selected1():
   selection = "Value = " + str(value.get())
   label.config(text = selection)
 
value = tk.DoubleVar()
scale = tk.Scale( window, from_ = 0, to=50,
            orient = tk.VERTICAL, variable = value )
scale.pack(anchor=tk.CENTER)

button = tk.Button(window, text="Get Slider Value", command=selected1)
button.pack(anchor=tk.CENTER)

label = tk.Label(window)
label.pack()

window.mainloop()

####################################################
#-- Wykład - ćwiczenia - z małą modyfikacją

# 2. aktualizacja automatyczna co 200 ms

import tkinter as tk

window = tk.Tk()

value = tk.DoubleVar()
scale = tk.Scale(window, from_= 0, to= 60,
        orient = tk.VERTICAL, variable = value)
scale.pack(anchor=tk.CENTER)

def selected():
    selection = "Value: " + str(value.get())
    label.config(text = selection)
    label.after(200, selected)

label = tk.Label(window)
label.pack()

selected()

window.mainloop()

####################################################
#-- Propozycja Copilot - z użyciem DoubleVar i lambda

import tkinter as tk
window = tk.Tk()

value = tk.DoubleVar()
scale = tk.Scale(window, from_=0, to=60,
                 orient=tk.VERTICAL, variable=value, command=lambda v: label.config(text=f"Value: {v}"))

scale.pack(anchor=tk.CENTER)
label = tk.Label(window, text=f"Value: {value.get()}")
label.pack()

window.mainloop()