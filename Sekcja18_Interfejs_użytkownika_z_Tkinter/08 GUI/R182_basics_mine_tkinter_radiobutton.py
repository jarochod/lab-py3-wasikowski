# R182. Tkinter - RadioButton

# RadioButton - pole radio

####################################################
#-- Wykład s1/1

# Widget typu radio pozwala tylko na zaznaczenie jednego z dostepnych elementów, wybór wykluca inne opcje. 
# Wybrana wartość będzie przechowana w radioValue i będzie liczbą całkowitą.

import tkinter as tk
window = tk.Tk()

def radioClicked1():
    print(radioValue.get())

radioValue = tk.IntVar()

radio1 = tk.Radiobutton(window, text='Option 1', 
        variable=radioValue, value=1, command=radioClicked1)
radio1.pack(anchor=tk.W)

radio2 = tk.Radiobutton(window, text='Option 2', 
        variable=radioValue, value=2, command=radioClicked1)
radio2.pack(anchor=tk.W)

window.mainloop()

####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

def radioClicked():
    print("radioValue: ", radioValue.get())

radioValue = tk.IntVar()

radio1 = tk.Radiobutton(window, text="Option 1", variable=radioValue,
                value=1, command=radioClicked)
radio2 = tk.Radiobutton(window, text="Option 2", variable=radioValue,
                value=2, command=radioClicked)
radio3 = tk.Radiobutton(window, text="Option 3", variable=radioValue,
                value=3, command=radioClicked)

radio1.pack()
radio2.pack()
radio3.pack()

window.mainloop()

####################################################
#-- Wykład - ćwiczenia - dodatkowe komentarze

# RadioButton - pole radio

import tkinter as tk
window = tk.Tk()

# Funkcja wywoływana po kliknięciu radiobutton
def radioCliked():
    print("radioValue:", radioValue.get())

# utworzenie zmiennej do przechowywania wartości radiobutton
radioValue = tk.StringVar()

# Ustawienie domyślnej wartości
radioValue.set("opcja 1")

# Utworzenie trzech radiobuttonów
# Każdy radiobutton ma przypisaną zmienną radioValue i unikalną wartość
# Funkcja radioCliked jest wywoływana po kliknięciu na którykolwiek z nich
radio1 = tk.Radiobutton(window, text="Option 1", variable=radioValue, value="opcja 1", command=radioCliked)
radio2 = tk.Radiobutton(window, text="Option 2", variable=radioValue, value="opcja 2", command=radioCliked)
radio3 = tk.Radiobutton(window, text="Option 3", variable=radioValue, value="opcja 3", command=radioCliked)

# Umieszczenie radiobuttonów w oknie
radio1.pack()
radio2.pack()
radio3.pack()

# Uruchomienie głównej pętli okna
window.mainloop()