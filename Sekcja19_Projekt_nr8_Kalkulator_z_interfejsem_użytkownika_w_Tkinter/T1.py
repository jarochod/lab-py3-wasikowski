import tkinter as tk

def main1():
    root = tk.Tk()
    root.title("Sterowanie Entry przez StringVar")

    # Tworzymy zmienną powiązaną z Entry
    entry_var = tk.StringVar()

    # Entry sterowane przez textvariable
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), width=30)
    entry.pack(pady=10)

    # Funkcja do dodawania tekstu
    def add_text(text):
        current = entry_var.get()
        entry_var.set(current + text)

    # Funkcja do czyszczenia pola
    def clear_text():
        entry_var.set("")

    # Przycisk dodający tekst "Hello"
    tk.Button(root, text="Dodaj 'Hello'", command=lambda: add_text("Hello")).pack(pady=5)

    # Przycisk dodający tekst "123"
    tk.Button(root, text="Dodaj '123'", command=lambda: add_text("123")).pack(pady=5)

    # Przycisk czyszczący pole
    tk.Button(root, text="Wyczyść", command=clear_text).pack(pady=5)

    root.mainloop()

main1()


##########################################

import tkinter as tk

def main2():
    root = tk.Tk()
    root.title("Sterowanie Entry przez StringVar")

    # Zmienna powiązana z Entry
    entry_var = tk.StringVar()

    # Pole tekstowe Entry
    entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), width=30)
    entry.pack(pady=10)

    # Jedna funkcja do obsługi wszystkich przycisków
    def button_click(value):
        if value == 'Clear':
            entry_var.set("")
        else:
            entry_var.set(entry_var.get() + value)

    # Lista przycisków (etykieta, wartość przekazywana do funkcji)
    buttons = [
        ("Dodaj 'Hello'", "Hello"),
        ("Dodaj '123'", "123"),
        ("Dodaj '+'", "+"),
        ("Wyczyść", "Clear")
    ]

    # Tworzenie przycisków dynamicznie
    for label, val in buttons:
        tk.Button(root, text=label, command=lambda v=val: button_click(v)).pack(pady=3)

    root.mainloop()

main2()
