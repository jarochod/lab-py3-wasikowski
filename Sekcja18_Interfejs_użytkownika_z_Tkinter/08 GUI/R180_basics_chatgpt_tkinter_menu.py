# R180. Tkinter - Menu aplikacji

####################################################
#-- ChatGPT - Tkinter Menu


# ✅ 1. Pętla + lambda (prosty, szybki styl)

import tkinter as tk

window = tk.Tk()

def menuItemSelected1(label):
    print(f"menu item selected: {label}")

def menuItemCloseSelected1():
    quit()

rootMenu = tk.Menu(window)

fileMenu = tk.Menu(rootMenu, tearoff=0)
for label in ["New", "Open", "Save", "Save as"]:
    fileMenu.add_command(label=label, command=lambda l=label: menuItemSelected1(l))
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=menuItemCloseSelected1)

editMenu = tk.Menu(rootMenu, tearoff=0)
for label in ["Cut", "Copy", "Paste", "Config"]:
    editMenu.add_command(label=label, command=lambda l=label: menuItemSelected1(l))

rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="Edit", menu=editMenu)

window.config(menu=rootMenu)
window.mainloop()


# ✅ 2. Słownik z labelami i funkcjami (bardziej zorganizowane)

import tkinter as tk

window = tk.Tk()

def menuItemSelected2(label):
    print(f"menu item selected: {label}")

def menuItemCloseSelected2():
    quit()

rootMenu = tk.Menu(window)

# Zdefiniuj zawartość menu jako słowniki
file_items = {
    "New": lambda: menuItemSelected2("New"),
    "Open": lambda: menuItemSelected2("Open"),
    "Save": lambda: menuItemSelected2("Save"),
    "Save as": lambda: menuItemSelected2("Save as"),
    "---": None,  # separator
    "Close": menuItemCloseSelected2
}

edit_items = {
    "Cut": lambda: menuItemSelected2("Cut"),
    "Copy": lambda: menuItemSelected2("Copy"),
    "Paste": lambda: menuItemSelected2("Paste"),
    "Config": lambda: menuItemSelected2("Config")
}

# Dodaj File menu
fileMenu = tk.Menu(rootMenu, tearoff=0)
for label, func in file_items.items():
    if label == "---":
        fileMenu.add_separator()
    else:
        fileMenu.add_command(label=label, command=func)

# Dodaj Edit menu
editMenu = tk.Menu(rootMenu, tearoff=0)
for label, func in edit_items.items():
    editMenu.add_command(label=label, command=func)

rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="Edit", menu=editMenu)

window.config(menu=rootMenu)
window.mainloop()



# ✅ 3. Styl klasowy (produkcyjny, skalowalny)

import tkinter as tk

class App:
    def __init__(self, root):
        self.window = root
        self.rootMenu = tk.Menu(root)
        self.window.config(menu=self.rootMenu)
        self.create_menus()

    def menuItemSelected(self, label):
        print(f"menu item selected: {label}")

    def menuItemCloseSelected(self):
        self.window.quit()

    def create_menus(self):
        fileMenu = tk.Menu(self.rootMenu, tearoff=0)
        for label in ["New", "Open", "Save", "Save as"]:
            fileMenu.add_command(label=label, command=lambda l=label: self.menuItemSelected(l))
        fileMenu.add_separator()
        fileMenu.add_command(label="Close", command=self.menuItemCloseSelected)

        editMenu = tk.Menu(self.rootMenu, tearoff=0)
        for label in ["Cut", "Copy", "Paste", "Config"]:
            editMenu.add_command(label=label, command=lambda l=label: self.menuItemSelected(l))

        self.rootMenu.add_cascade(label="File", menu=fileMenu)
        self.rootMenu.add_cascade(label="Edit", menu=editMenu)

root = tk.Tk()
app = App(root)
root.mainloop()



# ✅ Której wersji użyć?
# Styl	                Użycie	        Dla kogo / kiedy
# 1. Pętla + lambda	    ✔️	            Szybkie GUI, skrypty
# 2. Słownik + funkcje	✔️✔️           Gdy jest dużo opcji i chcesz ładny kod
# 3. Klasa + metody	    ✔️✔️✔️         Produkcja, rozbudowany GUI, testowalność

# Jeśli chcesz dodać np. skróty klawiszowe, ikony, dynamiczne włączanie/wyłączanie opcji — wersja klasowa jest najlepszą bazą.




# Kod bazowy z wykładu
####################################################
#-- Wykład - ćwiczenia
"""
import tkinter as tk

window = tk.Tk()

def menuItemSelected():
    print("menu item selected")

def menuItemCloseSelected():
    quit()

rootMenu = tk.Menu()
fileMenu = tk.Menu()
fileMenu.add_command(label="New", command=menuItemSelected)
fileMenu.add_command(label="Open", command=menuItemSelected)
fileMenu.add_command(label="Save", command=menuItemSelected)
fileMenu.add_command(label="Save as", command=menuItemSelected)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=menuItemCloseSelected)

editMenu = tk.Menu()
editMenu.add_command(label="Cut", command=menuItemSelected)
editMenu.add_command(label="Copy", command=menuItemSelected)
editMenu.add_command(label="Paste", command=menuItemSelected)
editMenu.add_command(label="Config", command=menuItemSelected)

rootMenu.add_cascade(label="File", menu=fileMenu)
rootMenu.add_cascade(label="Edit", menu=editMenu)

window.config(menu=rootMenu)

window.mainloop()
"""