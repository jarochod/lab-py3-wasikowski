# R178. Tkinter - checkbutton

####################################################
#-- Wykład s1/1

# CheckButton

import tkinter as tk
win = tk.Tk() 

def valueChanged1():
    if cbValue.get() == 0:
        print("checkbox not checked")
    elif cbValue.get() == 1:
        print("TOS accepted")

cbValue = tk.IntVar(value=1)
c1 = tk.Checkbutton(win, text="Accept TOS", variable=cbValue,
            onvalue=1, offvalue=0, command=valueChanged1)
c1.grid(row=0, sticky=tk.W)
c1.deselect()

tk.mainloop()

# Przycisk wyboru ma dwa stany włączony oraz wyłączony. Może posiadać różne wartości:
#  liczbowe intVar(), tekst - StringVar() lub wartość logiczną - BooleanVar()

# onValue - wartość pola jak jest zaznaczone
# offValue - wartość pola jak nie zaznaczone


####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

def valueChanged():
    if cbValue.get() == 0:
        print("CheckButton is off")
    if cbValue.get() == 1:
        print("CheckButton is on")

cbValue = tk.IntVar(value=0)
c1 = tk.Checkbutton(window, text="Accept TOS", variable=cbValue,
        onvalue=1, offvalue=0, command=valueChanged)
c1.grid(row=0)

window.mainloop()


####################################################
#-- chatgpt

import tkinter as tk  # Import biblioteki tkinter do tworzenia GUI

# Tworzenie głównego okna aplikacji
win = tk.Tk() 

# Funkcja, która zostanie wywołana po zmianie stanu checkboxa
def valueChanged2():
    # Sprawdzenie, jaka wartość jest aktualnie przypisana do cbValue (0 lub 1)
    if cbValue.get() == 0:
        print("checkbox not checked")  # Gdy checkbox jest odznaczony
    elif cbValue.get() == 1:
        print("TOS accepted")          # Gdy checkbox jest zaznaczony

# Zmienna kontrolna powiązana z checkboxem — przechowuje jego stan (1 = zaznaczony, 0 = odznaczony)
cbValue = tk.IntVar(value=1)  # Początkowa wartość to 1 (zaznaczony)

# Tworzenie widżetu Checkbutton (checkbox) i powiązanie go z cbValue
c1 = tk.Checkbutton(
    win,
    text="Accept TOS",        # Etykieta przy checkboxie
    variable=cbValue,         # Zmienna, która przechowuje stan checkboxa
    onvalue=1,                # Wartość przypisana do zmiennej, gdy zaznaczone
    offvalue=0,               # Wartość, gdy odznaczone
    command=valueChanged2     # Funkcja wywoływana przy zmianie stanu
)

# Umieszczenie checkboxa w siatce wierszy/kolumn, przyklejenie go do lewej strony (west)
c1.grid(row=0, sticky=tk.W)

# Odznaczenie checkboxa na starcie (mimo że IntVar ma wartość 1 — to ją nadpisuje)
c1.deselect()

# Uruchomienie pętli głównej aplikacji (czeka na zdarzenia i rysuje GUI)
tk.mainloop()