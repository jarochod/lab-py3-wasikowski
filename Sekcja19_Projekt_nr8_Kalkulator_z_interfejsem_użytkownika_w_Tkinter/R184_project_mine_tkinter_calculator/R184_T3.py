import tkinter as tk

window = tk.Tk()
window.title("Calculator")

# Definicja klasy kalkulatora
# Klasa ta tworzy prosty kalkulator z interfejsem graficznym w Tkinter
class Calculator:
    def __init__(self, win):
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ""
        self.calcKeyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", "Clear", "=", "/"]
        ]
        self.prepareGui(win)

    # Metoda odpowiedzialna za przygotowanie interfejsu graficznego kalkulatora
    def prepareGui(self, win):
        win.geometry("260x130")
        self.expressionField = tk.Entry(win, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=65)

        # Przygotowanie przycisków kalkulatora
        for rowIndex, calcRow in enumerate(self.calcKeyboard):
            for colIndex, buttonText in enumerate(calcRow):

                button = tk.Button(win, text=buttonText, height=1, width=8, fg="black", bg="silver",
                                   command=lambda v=buttonText: self.buttonPressed(v))
                button.grid(row=rowIndex + 1, column=colIndex)


    # Metoda wywoływana po naciśnięciu przycisku
    def buttonPressed(self, value):
        print(f"button pressed: {value}")
        if value == "Clear":
            self.expressionStr = ""
            self.equationStrVar.set("")
        elif value == "=":
            try:
                result = str(eval(self.expressionStr))
                self.equationStrVar.set(result)
                self.expressionStr = result
            except Exception:
                self.equationStrVar.set("Error")
                self.expressionStr = ""
        else:
            self.expressionStr += value
            self.equationStrVar.set(self.expressionStr)
        

# Tworzenie instancji kalkulatora i przekazanie głównego okna
calc = Calculator(window)

# Uruchomienie głównej pętli Tkinter
window.mainloop()


