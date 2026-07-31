# R181. Tkinter - Scale - suwak

# Widget slider pozwala na wybranie wartośći od from_ do to za pomocą wygodnego suwaka.
# Argument orient ma wartości tk.VERTICAL lub tk.HORIZONTAL

####################################################
# 1. Aktualizacja tylko po kliknięciu przycisku

import tkinter as tk

def run_test_1():
    window = tk.Toplevel(root)
    window.title("Test 1 – kliknięcie przycisku")
    
    def selected1():
        selection = "Value = " + str(value.get())
        label.config(text=selection)
    
    value = tk.DoubleVar()
    scale = tk.Scale(window, from_=0, to=50, orient=tk.VERTICAL, variable=value)
    scale.pack(anchor=tk.CENTER)

    button = tk.Button(window, text="Get Slider Value", command=selected1)
    button.pack(anchor=tk.CENTER)

    label = tk.Label(window)
    label.pack()


####################################################
# 2. Automatyczna aktualizacja co 200 ms (ćwiczenie z modyfikacją)

def run_test_2():
    window = tk.Toplevel(root)
    window.title("Test 2 – automatyczna aktualizacja")

    value = tk.DoubleVar()
    scale = tk.Scale(window, from_=0, to=60,
                     orient=tk.VERTICAL, variable=value)
    scale.pack(anchor=tk.CENTER)

    def selected():
        selection = "Value: " + str(value.get())
        label.config(text=selection)
        label.after(200, selected)

    label = tk.Label(window)
    label.pack()

    selected()


####################################################
# 3. Aktualizacja przy pomocy funkcji callback (propozycja ChatGPT)

def run_test_3():
    window = tk.Toplevel(root)
    window.title("Test 3 – funkcja callback")

    def update_label(val):
        label.config(text=f"Value: {val}")

    scale = tk.Scale(window, from_=0, to=60,
                     orient=tk.VERTICAL, command=update_label)
    scale.pack(anchor=tk.CENTER)

    label = tk.Label(window, text="Value: 0")
    label.pack()


####################################################
# 4. Użycie DoubleVar i lambda (propozycja Copilot)

def run_test_4():
    window = tk.Toplevel(root)
    window.title("Test 4 – DoubleVar i lambda")

    value = tk.DoubleVar()
    scale = tk.Scale(window, from_=0, to=60,
                     orient=tk.VERTICAL, variable=value,
                     command=lambda v: label.config(text=f"Value: {v}"))
    scale.pack(anchor=tk.CENTER)

    label = tk.Label(window, text=f"Value: {value.get()}")
    label.pack()


# Główne okno (tylko jedno Tk)
root = tk.Tk()
root.title("Wybór wersji testu")

tk.Label(root, text="Wybierz wersję testu z użyciem Scale:").pack(pady=10)

tk.Button(root, text="Test 1 – kliknięcie przycisku", command=run_test_1).pack(fill='x')
tk.Button(root, text="Test 2 – automatyczna aktualizacja", command=run_test_2).pack(fill='x')
tk.Button(root, text="Test 3 – funkcja callback", command=run_test_3).pack(fill='x')
tk.Button(root, text="Test 4 – DoubleVar i lambda", command=run_test_4).pack(fill='x')

root.mainloop()
