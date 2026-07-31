import tkinter as tk

class Calculator:
    """
    Klasa reprezentująca kalkulator graficzny.
    Obsługuje tworzenie interfejsu użytkownika i logikę obliczeń.
    """
    def __init__(self, master):
        """
        Konstruktor klasy Calculator.
        Inicjalizuje główne okno aplikacji i tworzy widżety.

        :param master: Główne okno Tkinter (root).
        """
        self.master = master
        master.title("Kalkulator")
        master.geometry("360x400")

        # Pole tekstowe do wyświetlania wprowadzonych danych i wyników
        self.entry = tk.Entry(master, width=16, font=('Arial', 26), borderwidth=2, relief='solid', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Definicja przycisków kalkulatora - ZMIANA TUTAJ
        self.button_defs = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), (',', 4, 1), ('=', 4, 2), ('+', 4, 3), # Zmieniono '.' na ','
        ]

        # Tworzenie przycisków i przypisywanie im akcji
        self.create_buttons()

    def on_button_click(self, char):
        """
        Obsługuje zdarzenia kliknięcia przycisków.
        W zależności od klikniętego znaku, dodaje go do pola wejścia
        lub wykonuje obliczenia.

        :param char: Znak (tekst) przypisany do klikniętego przycisku.
        """
        # Specjalna obsługa przecinka przed obliczeniem
        if char == '=':
            try:
                # Zamiana przecinka na kropkę dla funkcji eval(), która wymaga kropki jako separatora dziesiętnego
                expression = self.entry.get().replace(',', '.')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                # Jeśli wynik jest liczbą zmiennoprzecinkową, możemy formatować go z przecinkiem
                if isinstance(result, float):
                    self.entry.insert(tk.END, str(result).replace('.', ','))
                else:
                    self.entry.insert(tk.END, str(result))
            except Exception as e:
                # Obsługa błędów, np. nieprawidłowego wyrażenia
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Błąd")
        else:
            # Dodanie znaku do pola wejścia
            self.entry.insert(tk.END, char)

    def create_buttons(self):
        """
        Tworzy przyciski kalkulatora na podstawie listy button_defs
        i rozmieszcza je w siatce (grid).
        """
        for (text, row, col) in self.button_defs:
            button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

# Główna część programu
if __name__ == "__main__":
    root = tk.Tk()  # Tworzenie głównego okna Tkinter
    calculator = Calculator(root)  # Utworzenie instancji kalkulatora
    root.mainloop()  # Uruchomienie pętli zdarzeń Tkinter