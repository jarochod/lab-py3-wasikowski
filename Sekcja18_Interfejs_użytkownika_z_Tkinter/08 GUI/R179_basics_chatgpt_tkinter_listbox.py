# R179. Tkinter - ListBox lista przewijana z scrollbar

####################################################
#-- chatgpt

# Importujemy moduł tkinter i nadajemy mu alias 'tk'
import tkinter as tk

# Tworzymy główne okno aplikacji
window = tk.Tk()

# Tworzymy pionowy pasek przewijania (scrollbar)
scrollbar = tk.Scrollbar(window)

# Tworzymy listbox z możliwością wyboru wielu elementów jednocześnie (MULTIPLE)
listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

# Umieszczamy scrollbar po prawej stronie okna i rozciągamy go w pionie
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Umieszczamy listbox w oknie i rozciągamy go w pionie
listBox.pack(fill=tk.Y)

# Konfigurujemy scrollbar, aby sterował przewijaniem listBoxa
scrollbar.config(command=listBox.yview)

# Konfigurujemy listBox, aby informował scrollbar o zmianach pozycji (synchronizacja)
listBox.config(yscrollcommand=scrollbar.set)

# Wypełniamy listBox 15 elementami (liczby od 0 do 14)
for i in range(15):
    listBox.insert(tk.END, f"Opcja {i+1}")

# Tworzymy etykietę, która będzie wyświetlać wybrane elementy
label = tk.Label(window)
label.pack()

# Funkcja, która co 300 ms sprawdza zaznaczone elementy w listBoxie,
# wyciąga ich wartości (np. 'Opcja 1', 'Opcja 2'...) i aktualizuje tekst etykiety.
def checkList():
    selection = [listBox.get(i) for i in listBox.curselection()] # Pobiera wartości zaznaczone by stworzyć listę
    label.config(text=str(selection))   # Aktualizuje tekst etykiety
    label.after(300, checkList)         # Ustawia ponowne wywołanie funkcji po 300 ms

# Uruchamiamy cykliczne sprawdzanie zaznaczenia
checkList()

# Uruchamiamy główną pętlę aplikacji
window.mainloop()

####################################################
#-- chatgpt
# Nowa wersja kodu z obsługą zdarzenia <<ListboxSelect>> i print:

import tkinter as tk

window = tk.Tk()
scrollbar = tk.Scrollbar(window)
listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(fill=tk.Y)

scrollbar.config(command=listBox.yview)
listBox.config(yscrollcommand=scrollbar.set)

# Dodajemy 15 opcji do listy
for i in range(15):
    listBox.insert(tk.END, f"Opcja {i+1}")

label = tk.Label(window)
label.pack()

# Funkcja wywoływana automatycznie, gdy użytkownik zmieni zaznaczenie w listBoxie
def on_select(event):
    # listBox.curselection() zwraca krotkę z indeksami aktualnie zaznaczonych elementów (np. (1, 3, 4))
    # listBox.get(i) dla każdego indeksu i pobiera wartość tekstową przypisaną danemu wierszowi (np. "Opcja 2")
    selection = [listBox.get(i) for i in listBox.curselection()]

    # Aktualizacja treści etykiety label – wyświetla listę wybranych opcji (np. ['Opcja 2', 'Opcja 4'])
    label.config(text=str(selection))

    # Wydrukowanie listy zaznaczonych elementów do konsoli (np. w terminalu lub logu)
    print("Zaznaczone elementy:", selection)

# Podpinamy funkcję do zdarzenia zmiany zaznaczenia
listBox.bind('<<ListboxSelect>>', on_select)

window.mainloop()

# 🔍 Co się zmieniło?
# Zamiast cyklicznego sprawdzania (co 300 ms), używamy zdarzenia <<ListboxSelect>>, które automatycznie wywołuje funkcję, gdy użytkownik coś zaznaczy.
# Dzięki temu możemy łatwo wykonać dodatkową akcję, np. print(...).

'''
🧠 Co robi funkcja krok po kroku:
Reaguje na zdarzenie <<ListboxSelect>>:

Ta funkcja jest podpięta do zdarzenia, które występuje, gdy użytkownik zaznaczy lub odznaczy jakąś opcję w liście listBox.

Pobiera zaznaczone indeksy:
listBox.curselection() zwraca indeksy zaznaczonych pozycji w formie krotki, np. (0, 2, 3).

Zamienia indeksy na teksty:
listBox.get(i) zamienia każdy indeks i na odpowiadający mu napis, np. "Opcja 1", "Opcja 3", itd.
Całość zamieniana jest na listę nazw zaznaczonych opcji.

Aktualizuje label:
Etykieta label w GUI jest od razu aktualizowana i pokazuje zaznaczone elementy.

Dodatkowa akcja — print():
Program wypisuje listę zaznaczonych opcji w konsoli — może to służyć do debugowania lub dalszego przetwarzania.

'''