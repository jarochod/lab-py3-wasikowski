# R143. Tworzenie pakietów

# Pakiety - to hierarchiczna struktura plików z samodzielnym środowiskiem Pythona z modułami zwykle 
# wykonującym jakieś zadanie. Python udostępnia wiele pakietów stworzonych przez społeczność, które 
# można zainstalować dzięki instrukcji pip

import pack

print( pack.addNums(10,1) ) # 11
print( pack.subNums(10,1) ) # 9


book1 = pack.Book("Wakacje")
print( book1.title ) # Wakacje