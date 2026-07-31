# Wersja zmodyfikowana przez Gemini AI

import tkinter as tk

class Calculator:
    """
    Klasa reprezentująca prosty kalkulator GUI.
    """
    def __init__(self, master):
        """
        Inicjalizuje kalkulator.

        Args:
            master: Główne okno Tkinter (root).
        """
        self.master = master
        master.title("Kalkulator")
        master.geometry("183x195") # Ustawia rozmiar okna

        # Pole wejściowe dla wyświetlania i wprowadzania wyrażeń
        self.entry = tk.Entry(master, width=16, font=('Arial', 15), borderwidth=2, relief='solid', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

        # Definicja układu klawiatury kalkulatora
        self.calc_keyboard = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", "Clear", "=", "/"]
        ]

        # Tworzenie przycisków na podstawie definicji klawiatury
        self._create_buttons()

    def _create_buttons(self):
        """
        Tworzy i rozmieszcza przyciski kalkulatora w siatce.
        """
        for row_index, row_items in enumerate(self.calc_keyboard):
            for col_index, item in enumerate(row_items):
                # Tworzy przycisk i przypisuje do niego metodę on_button_click
                button = tk.Button(self.master, text=item, width=5, height=2,
                                   command=lambda char=item: self._on_button_click(char))
                # Rozmieszcza przycisk w siatce (dodajemy 1 do row_index, ponieważ wiersz 0 jest zajęty przez entry)
                button.grid(row=row_index + 1, column=col_index)

    def _on_button_click(self, char):
        """
        Obsługuje kliknięcia przycisków kalkulatora.

        Args:
            char (str): Znak lub operacja powiązana z klikniętym przyciskiem.
        """
        if char == '=':
            try:
                # Oblicza wyrażenie w polu wejściowym
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END) # Czyści pole
                self.entry.insert(tk.END, result) # Wstawia wynik
            except Exception as e:
                # W przypadku błędu wyświetla "Error"
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif char == 'Clear':
            # Czyści pole wejściowe
            self.entry.delete(0, tk.END)
        else:
            # Wstawia kliknięty znak do pola wejściowego
            self.entry.insert(tk.END, char)

# Główna część programu
if __name__ == "__main__":
    root = tk.Tk()
    # Tworzy instancję klasy Calculator
    my_calculator = Calculator(root)
    # Rozpoczyna pętlę zdarzeń Tkinter
    root.mainloop()