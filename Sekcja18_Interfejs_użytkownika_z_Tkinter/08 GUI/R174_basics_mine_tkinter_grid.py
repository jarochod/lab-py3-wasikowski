# R174. Tkinter - metoda grid do rozmieszczenia elementu w oknie

####################################################
#-- Wykład s1/1

# Metoda grid() - umieszcza elementy w dwuwymiarowej tabeli

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Name: ")
label1.grid(row=0, column=0, padx=2, pady=2)

label2 = tk.Label(window, text="Surname: ")
label2.grid(row=1, column=0, padx=2, pady=2)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=2, pady=2)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=2, pady=2)

window.mainloop()

# column - kolumna, domyślnie 0, czyli lewa kolumna
# row - wiersz, domyślnie 0, czyli na górze
# padx, pady - dopełnienie w osi x i y na około widgeta
# ipadx, ipady - dopełnienie wewnątrz
# columnspan - ile kolumn zajmuje widget, domyślnie 1
# rowspan - ile wierszy zajmuje widget, domyślnie 1


####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

b1 = tk.Button(window, bg="red", text="button 1")
b1.grid(row=0, column=0, ipadx=5, ipady=5)

b2 = tk.Button(window, bg="yellow", text="button 2")
b2.grid(row=0, column=1, ipadx=5, ipady=5)

b3 = tk.Button(window, bg="silver", text="button 3")
b3.grid(row=0, column=2, ipadx=5, ipady=5)


b4 = tk.Button(window, bg="silver", text="button 4")
b4.grid(row=1, column=0, ipadx=5, ipady=5)

b5 = tk.Button(window, bg="yellow", text="button 5")
b5.grid(row=1, column=1, ipadx=5, ipady=5)

b6 = tk.Button(window, bg="silver", text="button 6")
b6.grid(row=1, column=2, ipadx=5, ipady=5)

b7 = tk.Button(window, bg="silver", text="button 7")
# with rowspan use sticky="NS" north south to span widget from top to bottom
b7.grid(row=2, column=0, columnspan=3 , ipadx=5, ipady=5, sticky="EW")

window.mainloop()