# R40. Operatory przypiania - zadanie
#
# Zadanie - operacje na rachunku bankowym, skorzystaj 
# z skróconych operatorów przypisania z operacją
# matematyczną np:  +=  -=  *=  /=  itd
# Uwaga, po każdej operacji wyświetl saldo w konsoli
# 1) Stwórz zmienną balance z wartością początkową 1000
# 2) Dodaj wartość nowej pensji 7000
# 3) Odejmij 2000 kosztów za mieszkanie
# 4) Błąd banku pomnożył Twoje saldo trzykrotnie
# 5) Odejmij 4000 na komputer
# 6) Bank zorientował się że powstał błąd i cofa ostatnie           
#    transakcje. Dodaj do salda 4000, podziel je przez 3
#    i dopiero teraz odejmij 4000
# 7) Pokaż saldo końcowe

balance = 1000; print("Saldo początkowe:",balance) # Saldo początkowe: 1000
balance += 7000; print("Slado po wpływie pensji:",balance) # Slado po wpływie pensji: 8000
balance -= 2000; print("Saldo po opłaceniu mieszkania", balance) # Saldo po opłaceniu mieszkania 6000
balance *= 3; print("Saldo po pomyłce banku", balance) # Saldo po pomyłce banku 18000
balance -= 4000; print("Slado po zakupie komputera:", balance) # Slado po zakupie komputera: 14000
balance = (balance + 4000)/3 - 4000; print("Slado po naprawie błędu banku:", balance) # Slado po naprawie błedu banku: 2000.0







