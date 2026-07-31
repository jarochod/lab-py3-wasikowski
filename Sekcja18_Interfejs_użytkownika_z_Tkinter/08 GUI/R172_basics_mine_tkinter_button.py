# R172. Tkinter - Button przycisk

####################################################
#-- Wykład s1/1

# Button - przyciski

import tkinter as tk

window = tk.Tk()
window.title("Application") # tytuł okna
window.geometry("800x600") # ustawienie wymiarów okna

button = tk.Button(
    text="QUIT", # tekst na przycisku
    bd=10, # szerokość obramowania w pikselach / border in pixels
    bg="green", # kolor tła / background color
    fg="red", # kolor tekstu / text color
    command=quit, # funkcja wywoływana po kliknięciu / function when clicked
    activeforeground="white", # kolor tekstu po najechaniu kursorem / under cursor
    activebackground="silver", # kolor tła po najechaniu kursorem / under cursor
    font="Helvetica 16 bold italic underline", # czcionka / font
    height=3, # wysokość przycisku w linii tekstu / text lines height
    width=18, # szerokość przycisku w ilości znaków / text lines width
    justify=tk.CENTER, # wyrównanie tekstu / justify CENTER, LEFT, RIGHT
    padx=10, # padding tekstu z lewej i prawej strony / padding left and right to the text
    pady=10, # padding tekstu z góry i dołu / padding above and below the text
    relief="groove", # styl obramowania: sunken, raised, groove, ridge / border
)

button.pack() # umieszczenie przycisku w oknie / pack the button in the window




# Dodatkowe opcjonalne argumenty:
# state - DISABLED, ACTIVE, NORMAL 
# wraplength - dodatnia wartość określa, że tekst będzie zawijany aby zmieścić się w tej szerokości
# width - długość przycisku w ilości znaków jeśli tekst piksele jeśli obrazek
# Image - obrazek do wyświetlenia

# Tworzenie drugiego przycisku z dodatkowymi opcjonalnymi argumentami

button2 = tk.Button(
    text="This is a very long text that will wrap around to fit the button width.",
    bd=5,
    bg="blue",
    fg="white",
    state=tk.NORMAL, # stan przycisku: DISABLED, ACTIVE, NORMAL
    wraplength=100, # długość, po której tekst będzie zawijany
    width=30, # szerokość przycisku w ilości znaków
    font="Helvetica 10 bold",
    justify=tk.LEFT,
    padx=10,
    pady=10,
    relief="raised",
)

button2.pack()

window.mainloop() # uruchomienie głównej pętli okna / run the window main loop


####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()

def buttonClicked():
    print("clicked!")
    quit()

button = tk.Button(
    window,
    text="QUIT",
    bd=10,
    fg="red",
    bg="green",
    activeforeground="black",
    activebackground="silver",
    font="Times 18 bold",
    height=3,
    width=20,
    padx=10,
    pady=10,
    relief="groove",
    command = buttonClicked
)

button.pack()
window.mainloop()
