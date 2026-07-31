# R177. Tkinter - Text w wielu linijkach

####################################################
#-- Wykład s1/1

# Text

import tkinter as tk
win = tk.Tk()

scrollbar = tk.Scrollbar(win)
textBox = tk.Text(win,
    height=5, # height in lines
    width=20, # width in characters
    padx=10, # padding x, pixels
    pady=10, # padding y, pixels
    font="times 12 bold italic")

# scrollbar config regarding Text widget
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)

textBox.insert(tk.END, "Added text:\n line 1\n line 2\n line 3\n line 4\n line 5\n line 6")
print(f"Data from text: {textBox.get(1.0,"end")}")

win.mainloop()


# Widget Text wyświetla pole, gdzie użytkownik może wpisać tekst w wielu liniach.
# Metoda get() pobiera tekst z pola, wymaga podania pierwszego znaku 1.0, a koniec określa tekst “end” lub tk.END  
# np.  textBox.get(1.0,"end")



####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=5, width=30, padx=5, pady=5,
            font="Times 18 bold" )

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand = scrollbar.set)

textBox.insert(tk.END, "Hello World! \n Hello Again!")

print("Text data:", textBox.get(1.0, "end") )


window.mainloop()



####################################################
#-- chatgpt

# Text — użycie widżetu Text (wieloliniowego pola tekstowego)

import tkinter as tk  # Import biblioteki tkinter do tworzenia GUI

# Tworzenie głównego okna aplikacji
win = tk.Tk()

# Tworzenie paska przewijania (scrollbara) przypiętego do głównego okna
scrollbar = tk.Scrollbar(win)

# Tworzenie wieloliniowego pola tekstowego Text
textBox = tk.Text(win,
    height=5,           # Wysokość pola tekstowego — liczba wierszy (linijek tekstu)
    width=20,           # Szerokość pola tekstowego — liczba znaków w wierszu
    padx=10,            # Wewnętrzne marginesy poziome (odstęp od lewej/prawej krawędzi)
    pady=10,            # Wewnętrzne marginesy pionowe (odstęp od góry/dolnej krawędzi)
    font="times 12 bold italic"  # Czcionka: Times, rozmiar 12, pogrubiona i kursywa
)

# Ustawienie położenia scrollbara po prawej stronie i rozciągnięcie go na wysokość okna
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Ustawienie pola tekstowego po lewej stronie i rozciągnięcie go na wysokość
textBox.pack(side=tk.LEFT, fill=tk.Y)

# Powiązanie scrollbara z polem tekstowym — przewijanie będzie sterować zawartością textBox
scrollbar.config(command=textBox.yview)

# Powiązanie pola tekstowego z paskiem przewijania — pasek przewijania aktualizuje się w miarę wpisywania
textBox.config(yscrollcommand=scrollbar.set)

# Wstawienie tekstu do pola tekstowego
textBox.insert(tk.END, "\n".join([f"Linia {i}" for i in range(1, 21)]))

# Odczytanie i wypisanie zawartości pola tekstowego do konsoli (od wiersza 1, kolumny 0 do końca)
print(f"Data from text: {textBox.get(1.0, 'end')}")

# Uruchomienie pętli głównej aplikacji (czeka na zdarzenia i rysuje GUI)
win.mainloop()
