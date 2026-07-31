
"""
import tkinter as tk
root = tk.Tk()

root.title("Calculator")
root.geometry("183x195")

calc_keyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", "Clear", "=", "/"]
        ]

for row_index, row_items in enumerate(calc_keyboard):
    for col_index, item in enumerate(row_items):
        # Tworzy przycisk i przypisuje do niego metodę on_button_click
        button = tk.Button(root, text=item, width=5, height=2)
        # Rozmieszcza przycisk w siatce (dodajemy 1 do row_index, ponieważ wiersz 0 jest zajęty przez entry)
        button.grid(row=row_index + 1, column=col_index)

root.mainloop()
"""

import tkinter as tk
root = tk.Tk()

root.title("Calculator")
root.geometry("183x195")

calc_keyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", "Clear", "=", "/"]
        ]

for row_items in calc_keyboard:
    for item in row_items:
        button = tk.Button(root, text=item, width=5, height=2)
        button.grid(row=calc_keyboard.index(row_items), column=row_items.index(item))
        print(f"Button {item}, row {calc_keyboard.index(row_items)}, col {row_items.index(item)}")

root.mainloop()
