# R176. Tkinter - Entry pole tekstowe

####################################################
#-- Wykład s1/1
# Entry


import tkinter as tk

def showInfo():
    print("Name", el.get())


win = tk.Tk()

tk.Label(win, text="First Name").grid(row=0)
el = tk.Entry(win)
el.grid(row=0, column=1)

tk.Button(win, text="Sow", command=showInfo).grid(row=3, column=0)

win.mainloop()

# Widget Entry pozwala na wpisanie wartości, która później może być odczytana dzięki funkcji get()
# Wartość Entry można zmienić metodą insert() / e1.entry(0, “some value ”)
# Wartość Entry kasuje się metodą delete()


####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

tk.Label(window, text="First name:").grid(row=0, column=0)

entry = tk.Entry(window)
entry.grid(row=0, column=1)
entry.insert(0, "Hello")

def showData():
    print("Entry data:", entry.get() )
    entry.delete(0, "end")

tk.Button(window, text="show info", command=showData).grid(row=1)

window.mainloop()

####################################################
#-- mine/chatgpt 1z2

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Data 1")
label1.grid(row=0, column=0)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)
entry1.insert(0, "Hello")

label2 = tk.Label(window, text="Data 2")
label2.grid(row=1, column=0)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)
entry2.insert(0, "Warld!")

def getDel_(nameEntry, labelName):
    print(f"Entry data from {labelName}: {nameEntry.get()}")
    nameEntry.delete(0, "end")

# Używamy lambda, aby NIE wywołać funkcji od razu, tylko przekazać ją jako "gotową do wywołania".
# Dzięki temu argumenty entry1 i "Data 1" zostaną użyte dopiero PO kliknięciu przycisku.
button1 = tk.Button(window, text="Get/Del 1", command=lambda: getDel_(entry1, "Data 1"))
button1.grid(row=0, column=2)

# Analogicznie tutaj – lambda tworzy funkcję, która wywoła getDel_ z entry2 i "Data 2" po kliknięciu.
button2 = tk.Button(window, text="Get/Del 2", command=lambda: getDel_(entry2, "Data 2"))
button2.grid(row=1, column=2)

window.mainloop()

####################################################
#-- mine/chatgpt 2z2

import tkinter as tk
from functools import partial

window = tk.Tk()

label1 = tk.Label(window, text="Data 1")
label1.grid(row=0, column=0)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)
entry1.insert(0, "Hello")

label2 = tk.Label(window, text="Data 2")
label2.grid(row=1, column=0)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)
entry2.insert(0, "Warld!")

def getDel(entry_widget, label_name):
    print(f"Entry data from {label_name}: {entry_widget.get()}")
    entry_widget.delete(0, "end")

# Tworzymy funkcje z partialem – każda "zapamięta" swoje argumenty
getDel1 = partial(getDel, entry1, "Data 1")
getDel2 = partial(getDel, entry2, "Data 2")

# Ustawiamy je jako command
button1 = tk.Button(window, text="Get/Del 1", command=getDel1)
button1.grid(row=0, column=2)

button2 = tk.Button(window, text="Get/Del 2", command=getDel2)
button2.grid(row=1, column=2)

window.mainloop()
