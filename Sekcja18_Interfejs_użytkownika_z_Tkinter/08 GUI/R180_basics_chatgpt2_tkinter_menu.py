# R180. Tkinter - Menu aplikacji

####################################################
#-- ChatGPT - Tkinter Menu

# ✅ 3. Styl klasowy (produkcyjny, skalowalny) + skróty klawiszowe

import tkinter as tk

class App:
    def __init__(self, root):
        self.window = root
        self.window.title("Menu Example with Shortcuts")
        self.rootMenu = tk.Menu(root)
        self.window.config(menu=self.rootMenu)
        self.create_menus()
        self.bind_shortcuts()

    def menuItemSelected(self, label):
        print(f"menu item selected: {label}")

    def menuItemCloseSelected(self):
        self.window.quit()

    def create_menus(self):
        # File menu
        fileMenu = tk.Menu(self.rootMenu, tearoff=0)
        fileMenu.add_command(label="New\tCtrl+N", command=lambda: self.menuItemSelected("New"))
        fileMenu.add_command(label="Open", command=lambda: self.menuItemSelected("Open"))
        fileMenu.add_command(label="Save\tCtrl+S", command=lambda: self.menuItemSelected("Save"))
        fileMenu.add_command(label="Save as", command=lambda: self.menuItemSelected("Save as"))
        fileMenu.add_separator()
        fileMenu.add_command(label="Close\tCtrl+Q", command=self.menuItemCloseSelected)

        # Edit menu
        editMenu = tk.Menu(self.rootMenu, tearoff=0)
        for label in ["Cut", "Copy", "Paste", "Config"]:
            editMenu.add_command(label=label, command=lambda l=label: self.menuItemSelected(l))

        self.rootMenu.add_cascade(label="File", menu=fileMenu)
        self.rootMenu.add_cascade(label="Edit", menu=editMenu)

    def bind_shortcuts(self):
        self.window.bind("<Control-n>", lambda event: self.menuItemSelected("New"))
        self.window.bind("<Control-s>", lambda event: self.menuItemSelected("Save"))
        self.window.bind("<Control-o>", lambda event: self.menuItemSelected("Open"))
        self.window.bind("<Control-q>", lambda event: self.menuItemCloseSelected())

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