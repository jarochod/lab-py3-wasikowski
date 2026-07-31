# R179. Tkinter - ListBox lista przewijana z scrollbar

####################################################
#-- chatgpt - rozbudowany przykład

import tkinter as tk

# Tworzymy główne okno aplikacji
window = tk.Tk()
window.title("Rozszerzony przykład listy przewijanej")

# Pasek przewijania
scrollbar = tk.Scrollbar(window)
listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listBox.yview)
listBox.config(yscrollcommand=scrollbar.set)

# Dodajemy 15 opcji
for i in range(15):
    listBox.insert(tk.END, f"Opcja {i+1}")

# Etykieta pokazująca listę zaznaczonych opcji
label = tk.Label(window, text="Zaznaczenie: []")
label.pack()

# Pole tekstowe do wyświetlania szczegółów zaznaczonych opcji
details = tk.Text(window, height=10, width=40)
details.pack()

# Przykładowe dane opisujące każdą opcję
opisy_opcji = {
    f"Opcja {i+1}": f"To jest szczegółowy opis dla opcji {i+1}." for i in range(15)
}

# Funkcja wywoływana po zmianie zaznaczenia
def on_select(event):
    selection = [listBox.get(i) for i in listBox.curselection()]
    label.config(text=f"Zaznaczenie: {selection}")
    print("Zaznaczone elementy:", selection)

    # Czyszczenie pola tekstowego
    details.delete('1.0', tk.END)

    # Dodanie opisu dla każdej zaznaczonej opcji
    for opcja in selection:
        opis = opisy_opcji.get(opcja, "Brak opisu.")
        details.insert(tk.END, f"{opcja}:\n{opis}\n\n")

# Powiązanie zdarzenia zaznaczenia z funkcją
listBox.bind('<<ListboxSelect>>', on_select)

window.mainloop()