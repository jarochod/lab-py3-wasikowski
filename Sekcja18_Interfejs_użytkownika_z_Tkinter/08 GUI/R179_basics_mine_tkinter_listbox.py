# R179. Tkinter - ListBox lista przewijana z scrollbar

####################################################
#-- Wykład s1/1

# Listbox - lista przewijana z scrollbar

import tkinter as tk
window = tk.Tk()

scrollbar = tk.Scrollbar(window)
listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

# scrollbar for vertical axis - Y
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(fill=tk.Y) # fill vertically

# set scrollbar for vertcal scrolling of listbox
scrollbar.config(command = listBox.yview)
# set vertical scrolling for listbox to set method
listBox.config(yscrollcommand = scrollbar.set)

for i in range(20):
   listBox.insert(tk.END, str(i))

lab = tk.Label(window)

def checkList_():
    lab.after(300, checkList_)
    selection = listBox.curselection()
    lab.config(text = str(selection))

lab.pack() 
checkList_()

tk.mainloop()

####################################################
#-- Wykład - ćwiczenia

import tkinter as tk

window = tk.Tk()
scrollbar = tk.Scrollbar(window)

listBox = tk.Listbox(window, selectmode=tk.MULTIPLE)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(fill=tk.Y)
scrollbar.config(command = listBox.yview)
listBox.config(yscrollcommand= scrollbar.set)

for i in range(15):
    listBox.insert(tk.END, str(i))

label = tk.Label(window)
label.pack()

def checkList():
    selection = listBox.curselection()
    label.config(text = str(selection))
    label.after(300, checkList)

checkList()
window.mainloop()