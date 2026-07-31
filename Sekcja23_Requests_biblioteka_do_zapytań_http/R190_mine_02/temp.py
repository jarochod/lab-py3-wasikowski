import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Konwenter walut")

        # Kursy walut zapisane jako atrybut obiektu
        self.currency_rates = self.fetch_currency_rates()

        # Utworzenie UI
        self.create_widgets()

        # Od razu pokazanie obliczeń
        self.calculate()

    def fetch_currency_rates(self) -> dict:
        # Tu w prawdziwym programie pobierałbyś dane z API
        # Na razie robimy "na sztywno" słownik
        return {
            "USD": 4.1,
            "EUR": 4.5,
            "GBP": 5.2,
        }

    def create_widgets(self) -> None:
        self.label = tk.Label(self.root, text="Przykładowy konwerter")
        self.label.pack(pady=10)

    def calculate(self) -> None:
        # Użycie self.currency_rates
        usd = self.currency_rates["USD"]
        eur = self.currency_rates["EUR"]
        gbp = self.currency_rates["GBP"]
        self.label.config(text=f"1 USD = {usd} PLN | 1 EUR = {eur} PLN | 1 GBP = {gbp} GBP")

root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()