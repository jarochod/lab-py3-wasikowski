# R180. Tkinter - Menu aplikacji

####################################################
#-- Wykład s1/1

# Menu w kodzie zaczyna się od elementu rootMenu połączonego z window. 
# Do rootMenu dołączone będzie fileMenu. 
# Następnie fileMenu posiada wszystkie elementy.

import tkinter as tk
window = tk.Tk()

def menuItemSelected_():
    print("menuItemselected_")

def menuItemCloseSelected_():
    quit()

rootMenu = tk.Menu(window) # root menu
fileMenu = tk.Menu(rootMenu) # add fileMenu to root menu

fileMenu.add_command(label="New", command=menuItemSelected_)
fileMenu.add_command(label="Open", command=menuItemSelected_) 
fileMenu.add_command(label="Save as...", command=menuItemSelected_)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=menuItemCloseSelected_)

# add fileMenu to rootMenu with Label
rootMenu.add_cascade(label="File", menu=fileMenu)

window.config(menu=rootMenu) # add rootMenu to window

window.mainloop()



####################################################
#-- Wykład - ćwiczenia - z moimi modyfikacjami

import tkinter as tk
window = tk.Tk()

def menuItemSelected(label):
    print("Selected menu item:", label)  # Funkcja wywoływana po kliknięciu opcji menu (poza Exit)

window.title("Menu aplikacji")  # Tytuł okna
window.geometry("400x300")      # Rozmiar okna

rootMenu = tk.Menu(window)  # Główne menu aplikacji (kontener dla menu File i Edit)

# Tworzenie menu "File"
fileMenu = tk.Menu(rootMenu, tearoff=0)  # tearoff=0 zapobiega odczepianiu menu (standard w nowoczesnych GUI)
Labels_menu = ["New", "Open", "Save", "Exit"]
fileMenu.add_command(label=Labels_menu[0], command=lambda: menuItemSelected(Labels_menu[0]))
fileMenu.add_command(label=Labels_menu[1], command=lambda: menuItemSelected(Labels_menu[1]))
fileMenu.add_command(label=Labels_menu[2], command=lambda: menuItemSelected(Labels_menu[2]))
fileMenu.add_separator()  # Oddzielenie pozycji Exit od pozostałych
fileMenu.add_command(label=Labels_menu[3], command=window.quit)  # Zamyka aplikację

# Tworzenie menu "Edit"
editMenu = tk.Menu(rootMenu, tearoff=0)
Labels_edit = ["Cut", "Copy", "Paste", "Config"]
editMenu.add_command(label=Labels_edit[0], command=lambda: menuItemSelected(Labels_edit[0]))
editMenu.add_command(label=Labels_edit[1], command=lambda: menuItemSelected(Labels_edit[1]))
editMenu.add_command(label=Labels_edit[2], command=lambda: menuItemSelected(Labels_edit[2]))
editMenu.add_command(label=Labels_edit[3], command=lambda: menuItemSelected(Labels_edit[3]))

# Dodanie obu podmenu do głównego menu
rootMenu.add_cascade(label="File", menu=fileMenu)  # Podmenu "File"
rootMenu.add_cascade(label="Edit", menu=editMenu)  # Podmenu "Edit"

window.config(menu=rootMenu)  # Ustawienie menu dla głównego okna

window.mainloop()  # Uruchomienie pętli zdarzeń aplikacji



"""
Zawsze używaj jawnych parametrów:

rootMenu = tk.Menu(window)
fileMenu = tk.Menu(rootMenu, tearoff=0)
editMenu = tk.Menu(rootMenu, tearoff=0)

Dzięki temu:
-aplikacja jest bardziej przewidywalna,
-kod jest czytelniejszy,
-unikniesz subtelnych błędów przy większych aplikacjach GUI.

Uwaga tearoff=0 zapobiega "odrywalności" menu
"""

