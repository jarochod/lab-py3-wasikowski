# R184. Kalkulator w Tkinter

# Import biblioteki tkinter i nadanie jej aliasu 'tk'
import tkinter as tk

# Tworzenie głównego okna aplikacji
window = tk.Tk()
window.title("Calculator")  # Ustawienie tytułu okna

# Definicja klasy kalkulatora
class Calculator:
    def __init__(self, win):
        # Zmienna przechowująca wyrażenie matematyczne jako StringVar (do połączenia z polem tekstowym)
        self.equationStrVar = tk.StringVar()
        
        # Wyrażenie w postaci zwykłego łańcucha znaków
        self.expressionStr = ""
        
        # Definicja klawiatury kalkulatora jako lista list przycisków
        self.calcKeyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0","Clear","=", "/"]
        ]
        
        # Wywołanie metody odpowiedzialnej za przygotowanie interfejsu GUI
        self.prepareGui(win)

    # Metoda tworząca interfejs graficzny
    def prepareGui(self, win):
        # Ustawienie rozmiaru okna
        win.geometry("260x130")
        
        # Pole do wyświetlania wprowadzanego wyrażenia i wyników
        self.expressionField = tk.Entry(win, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=60)  # Rozciągnięcie pola na 4 kolumny

        # Pętla po wierszach klawiatury kalkulatora
        rowIndex = 0
        while rowIndex < len(self.calcKeyboard):
            calcRow = self.calcKeyboard[rowIndex]

            # Pętla po przyciskach w danym wierszu
            columnIndex = 0
            while columnIndex < len(calcRow):
                buttonText = calcRow[columnIndex]

                # Tworzenie przycisku z przypisaną akcją po kliknięciu
                button = tk.Button(win, text=buttonText, height=1, width=8, fg="black", 
                                   bg="silver", command=lambda v=buttonText: self.buttonPressed(v))
                button.grid(row=rowIndex+1, column=columnIndex)  # Umieszczenie przycisku w siatce

                columnIndex += 1
            rowIndex += 1

    # Metoda wywoływana po naciśnięciu przycisku
    def buttonPressed(self, value):
        print("button pressed:", value)  # Debug: wypisanie wciśniętego przycisku

        if value == "Clear":
            # Wyczyść pole i zmienne
            self.expressionStr = ""
            self.equationStrVar.set("")
            return
        
        if value == "=":
            # Oblicz wynik wyrażenia i wyświetl go
            result = str(eval(self.expressionStr))  # UWAGA: eval jest niebezpieczne w aplikacjach produkcyjnych
            self.expressionStr = result
            self.equationStrVar.set(result)
            return

        # Dodaj wartość do wyrażenia i odśwież pole tekstowe
        self.expressionStr += str(value)
        self.equationStrVar.set(self.expressionStr)

# Utworzenie instancji kalkulatora i uruchomienie pętli głównej aplikacji
calc = Calculator(window)
window.mainloop()
