# R173. Tkinter - metoda pack do ustawienia elementu w oknie

####################################################
#-- Wykład s1/2

# Metoda pack() - umożliwia rozmieszczenie elementów w blokach wewnątrz okna.

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Information text #1")
label1.pack(side=tk.TOP, expand=True)

label2 = tk.Label(window, text="Nex information text #2")
label2.pack(side=tk.TOP, expand=True)

label3 = tk.Label(window, text="Botton information text #3")
label3.pack(side=tk.BOTTOM, expand=True)

button1 = tk.Button(window, text="Opt 1", fg="red")
button1.pack(side=tk.LEFT)

button2 = tk.Button(window, text="Opt 2", fg="blue")
button2.pack(side=tk.RIGHT)

window.mainloop()

# Opcje:
# expand - jeśli true widget rozszerza się na dostępną przestrzeń 
# fill - czy widget wypełni dodatkową przestrzeń albo zajmie minimalną przestrzeń - None - domyślnie.
        # X - wypełni się horyzontalnie
        # Y - wertykalnie, 
        # Both - obie,
# side - strona: TOP, BOTTOM. LEFT, RIGHT


#-- Wykład s2/2

# Metoda pack() - fill pozwala na wypełnienie dodatkowej przestrzeni, 
# która np pojawi się przy powiększeniu okna

window = tk.Tk()

label1 = tk.Label(window, background="red", text="Top Information text #1")
label1.pack(fill=tk.BOTH, side=tk.TOP, expand=tk.TRUE)

label2 = tk.Label(window, background="yellow", text="Top information text #2")
label2.pack(fill=tk.BOTH, side=tk.TOP, expand=tk.TRUE)

label3 = tk.Label(window, background="green", text="Bottom information text #3")
label3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=tk.TRUE)

button1 = tk.Button(window, background="red", text="Opt 1", fg="black")
button1.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)

button2 = tk.Button(window, background="green", text="Opt 2", fg="black")
button2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.TRUE)

window.mainloop()

####################################################
#-- Wykład - ćwiczenia


import tkinter as tk
window = tk.Tk()

label1 = tk.Label(window, text="Label 1", bg="red")
label1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

label2 = tk.Label(window, text="Label 2", bg="silver")
label2.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

button1 = tk.Button(window, bg="red", text="button 1")
button1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

button2 = tk.Button(window, bg="yellow", text="button 2")
button2.pack(side=tk.RIGHT, expand=True, fill=tk.Y)

window.mainloop()


####################################################
#-- chatgpt


import tkinter as tk

window = tk.Tk()
window.geometry("400x300")  # Ustawiamy rozmiar okna

# Label rozciągnięty w poziomie
label1 = tk.Label(window, text="Information text #1", bg="lightgrey")
label1.pack(side=tk.TOP, expand=True, fill='x')  # fill='x' – rozciąga się w poziomie

# Label rozciągnięty w pionie
label2 = tk.Label(window, text="Next information text #2", bg="lightblue")
label2.pack(side=tk.LEFT, expand=True, fill='y')  # fill='y' – rozciąga się w pionie

# Label rozciągnięty w obu kierunkach
label3 = tk.Label(window, text="Bottom information text #3", bg="lightgreen")
label3.pack(side=tk.RIGHT, expand=True, fill='both')  # fill='both' – pełne rozciągnięcie

# Button rozciągnięty w poziomie u dołu
button1 = tk.Button(window, text="Opt 1", fg="red", bg="white")
button1.pack(side=tk.BOTTOM, fill='x')

# Kolejny button u dołu, też rozciągnięty w poziomie
button2 = tk.Button(window, text="Opt 2", fg="blue", bg="white")
button2.pack(side=tk.BOTTOM, fill='x')

# Przycisk bez expand i fill (rozmiar minimalny), zgodny z Pylance
button3 = tk.Button(window, text="No expand", fg="black", bg="lightyellow")
button3.pack(side=tk.TOP, expand=False, fill='none')  # fill='none' zamiast None

window.mainloop()
