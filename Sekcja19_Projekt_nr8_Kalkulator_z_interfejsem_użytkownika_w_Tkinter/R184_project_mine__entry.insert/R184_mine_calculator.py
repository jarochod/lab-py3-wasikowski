
import tkinter as tk
root = tk.Tk()

root.title("Calculator")
root.geometry("183x195")

entry = tk.Entry(root, width=16, font=('Arial', 15), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=1, pady=1)


def on_button_click(char):
    if char == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == 'Clear':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)


calcKeyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0","Clear","=", "/"]
        ]

rowIndex = 0
while rowIndex < len(calcKeyboard):
    row = calcKeyboard[rowIndex]
    columnIndex = 0
    while columnIndex < len(row):
        item = row[columnIndex]
        button = tk.Button(root, text=item, width=5, height=2, command=lambda char=item: on_button_click(char))
        button.grid(row=rowIndex+1, column=columnIndex)
        columnIndex += 1
    rowIndex += 1


root.mainloop()