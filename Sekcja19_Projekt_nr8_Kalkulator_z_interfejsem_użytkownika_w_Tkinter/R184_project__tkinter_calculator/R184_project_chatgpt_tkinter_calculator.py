# R184. Kalkulator w Tkinter

import tkinter as tk # Importowanie biblioteki tkinter, która służy do tworzenia graficznych interfejsów użytkownika (GUI).

# Tworzenie głównego okna aplikacji.
window = tk.Tk()
window.title("Kalkulator") # Ustawienie tytułu okna aplikacji.

class Calculator:
    # Metoda inicjalizacyjna klasy Calculator. Wywoływana przy tworzeniu nowego obiektu Calculator.
    def __init__(self, win):
        # Zmienna StringVar z tkinter, która będzie powiązana z polem tekstowym (Entry)
        # i automatycznie aktualizować jego zawartość.
        self.equationStrVar = tk.StringVar()
        # Zwykły string Pythona, który będzie przechowywał całe wyrażenie matematyczne
        # wprowadzane przez użytkownika (np. "12+3*4").
        self.expressionStr = ""
        # Definicja układu klawiatury kalkulatora w postaci listy list.
        self.calcKeyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0","Clear","=", "/"] # "Clear" do czyszczenia, "=" do obliczania wyniku.
        ]
        # Wywołanie metody prepareGui, aby zbudować interfejs użytkownika.
        self.prepareGui(win)

    # Metoda odpowiedzialna za przygotowanie i rozmieszczenie elementów GUI w oknie.
    def prepareGui(self, win):
        win.geometry("260x130") # Ustawienie rozmiaru okna (szerokość x wysokość).
        # Tworzenie pola tekstowego (Entry) na górze okna, gdzie będzie wyświetlane wyrażenie/wynik.
        # textvariable=self.equationStrVar sprawia, że zawartość pola jest powiązana z self.equationStrVar.
        self.expressionField = tk.Entry(win, textvariable=self.equationStrVar)
        # Rozmieszczenie pola tekstowego. columnspan = 4 sprawia, że pole zajmuje 4 kolumny.
        # ipadx = 60 dodaje wewnętrzny padding poziomy.
        self.expressionField.grid(columnspan = 4, ipadx = 60)

        rowIndex = 0 # Inicjalizacja indeksu wiersza dla przycisków.
        # Pętla iterująca po każdym wierszu zdefiniowanym w calcKeyboard.
        while rowIndex < len(self.calcKeyboard):
            calcRow = self.calcKeyboard[rowIndex] # Pobranie bieżącego wiersza przycisków.

            columnIndex = 0 # Inicjalizacja indeksu kolumny dla przycisków.
            # Pętla iterująca po każdym elemencie (przycisku) w bieżącym wierszu.
            while columnIndex < len(calcRow):
                buttonText = calcRow[columnIndex] # Pobranie tekstu dla bieżącego przycisku.
                # Tworzenie przycisku.
                # text: tekst wyświetlany na przycisku.
                # height, width: rozmiary przycisku.
                # fg, bg: kolory tekstu i tła przycisku.
                # command: funkcja, która zostanie wywołana po naciśnięciu przycisku.
                # lambda v=buttonText: self.buttonPressed(v) używa lambdy do przekazania
                # wartości buttonText do metody buttonPressed. Jest to ważne, aby każdemu
                # przyciskowi przypisać jego unikalną wartość.
                button = tk.Button(win, text=buttonText, height = 1, width = 8, fg="black", 
                                bg="silver", command = lambda v=buttonText: self.buttonPressed(v) )
                # Rozmieszczenie przycisku w siatce. rowIndex+1, ponieważ rząd 0 jest zajęty przez pole Entry.
                button.grid(row = rowIndex+1, column = columnIndex)
                columnIndex += 1 # Przejście do następnej kolumny.

            rowIndex += 1 # Przejście do następnego wiersza.

    # Metoda wywoływana, gdy użytkownik naciśnie przycisk.
    def buttonPressed(self, value):
        print("przycisk naciśnięty:", value) # Wyświetlanie w konsoli, który przycisk został naciśnięty (do debugowania).

        # Obsługa przycisku "Clear".
        if value == "Clear":
            self.expressionStr = "" # Wyczyszczenie zapisanego wyrażenia.
            self.equationStrVar.set("") # Wyczyszczenie tekstu w polu wyświetlania.
            return # Zakończenie funkcji.
        
        # Obsługa przycisku "=".
        if value == "=":
            try: # Użycie bloku try-except do obsługi potencjalnych błędów obliczeniowych (np. dzielenie przez zero).
                # Obliczenie wyniku wyrażenia za pomocą funkcji eval().
                # eval() interpretuje string jako kod Pythona i wykonuje go.
                # W tym przypadku oblicza wyrażenie matematyczne.
                result = str( eval(self.expressionStr) )
                self.expressionStr = result # Ustawienie wyniku jako bieżące wyrażenie.
                self.equationStrVar.set(result) # Wyświetlenie wyniku w polu.
            except Exception as e:
                self.equationStrVar.set("Błąd") # Wyświetlenie komunikatu o błędzie.
                self.expressionStr = "" # Wyczyszczenie wyrażenia po błędzie.
            return # Zakończenie funkcji.

        # Dla cyfr i operatorów:
        self.expressionStr += str(value) # Dodanie naciśniętej wartości do bieżącego wyrażenia.
        self.equationStrVar.set( self.expressionStr ) # Zaktualizowanie pola wyświetlania.


# Tworzenie obiektu kalkulatora, przekazując mu główne okno Tkinter.
calc = Calculator(window)
# Uruchomienie głównej pętli zdarzeń Tkinter. Ten wiersz musi być ostatni,
# ponieważ utrzymuje okno otwarte i reaguje na interakcje użytkownika.
window.mainloop()