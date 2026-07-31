# R183. Tkinter - SpinBox czyli wartość z zakresu


####################################################
#-- Wykład s1/1

# SpinBox - kontrolka do ustawiania wartości z określonego zakresu

import tkinter as tk

window = tk.Tk()

def update_label():
    label.config(text="Wartość: " + str(spin.get()))

spin = tk.Spinbox(window, from_ = 0, to = 20, command=update_label)
spin.pack()


label = tk.Label(window, text="Wartość: " + str(spin.get()))
label.pack()

window.mainloop()

####################################################
#-- Wykład - ćwiczenia - dodatkowe komentarze, małe zmiany

import tkinter as tk

window = tk.Tk()

# funkcja aktualizująca etykietę przy zmianie wartości SpinBoxa
def spinValue():
    label.config(text="Wartość: " + str(spin.get()))

# Ustawienie zakresu wartości SpinBoxa od 0 do 50, z krokiem 1
spin = tk.Spinbox(window, from_=0, to=50, command=spinValue)
spin.pack()

# Etykieta do wyświetlania aktualnej wartości SpinBoxa, aktualizowana przy zmianie wartości SpinBoxa
label = tk.Label(window, text="Wartość: " + str(spin.get()))
label.pack()


window.mainloop()