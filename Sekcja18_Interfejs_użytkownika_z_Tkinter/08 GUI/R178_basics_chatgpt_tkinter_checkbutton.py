# R178. Tkinter - checkbutton

# CheckButton

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


####################################################
#-- chatgpt - przykład z realnym użyciem

# Funkcionalność kodu "Z oknem Rejestracja":
# 1. Wyświetla CheckButton „Akceptuję regulamin”.
# 2. Uaktywnia przycisk „Dalej” po zaznaczeniu.
# 3. Po kliknięciu „Dalej” zamyka okno.

import tkinter as tk

window = tk.Tk()
window.title("Rejestracja")

# Funkcja: aktywuje lub dezaktywuje przycisk "Dalej"
def toggleNextButton():
    if cbValue.get() == 1:
        nextButton.config(state="normal")
    else:
        nextButton.config(state="disabled")

# Funkcja: po kliknięciu "Dalej" zamyka okno
def proceed():
    window.destroy()  # zamyka okno główne

# Zmienna powiązana z CheckButton
cbValue = tk.IntVar(value=0)

# CheckButton – akceptacja regulaminu
check = tk.Checkbutton(window, text="Akceptuję regulamin", variable=cbValue, command=toggleNextButton)
check.pack(pady=10)

# Przycisk "Dalej" – na początku wyłączony
nextButton = tk.Button(window, text="Dalej", state="disabled", command=proceed)
nextButton.pack(pady=10)

window.mainloop()

# 🧪 Jak to działa?
# Kiedy klikniesz CheckButton, uruchamiana jest funkcja toggleNextButton().
# Przycisk „Dalej” staje się aktywny tylko, jeśli zaznaczysz akceptację.
# Po kliknięciu „Dalej”, funkcja proceed() zamyka okno (window.destroy()).