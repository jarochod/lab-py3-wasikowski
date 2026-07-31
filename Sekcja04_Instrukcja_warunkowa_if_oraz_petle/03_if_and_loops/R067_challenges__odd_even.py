# R67. for oraz instrukcja if - odd, even - zadanie

# Zdanie z listą liczb od -4 do 4
# 1) Wyświetl w konsoli następujące informacje z użyciem pętli na liście 
#    oraz instrukcji if elif else w celu sprawdzenia, czy liczba jest parzysta
#    czy nieparzysta, oczywiście dodaj informacje w konsoli.
# 2) Pamiętaj, że 0 będzie oddzielnym przypadkiem, który musisz sprawdzić jako
#    pierwszy w if i w jej bloku napisz w konsoli tekst: "Zero jest parzyste".
#    Następnie w elif sprawdz czy liczba jest parzysta, a oczywiście w else
#    bedzie pewność, że jest nieparzysta.

numbers = [-4,-3,-2,-1,0,1,2,3,4]

for n in numbers:
    if n == 0:
        print(n,"zero jest parzyste")
    elif n % 2 == 0:
        print(n, "jest parzysta")
    else:
        print(n, "jest nieparzysta")

