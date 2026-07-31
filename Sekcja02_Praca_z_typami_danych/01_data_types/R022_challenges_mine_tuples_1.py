# R22. Tuples - zadanie 1

# 1. Stwórz krotkę z wartościami: 50, 100, 150, 200, 250 
# 2. Pokaż typ krotki w konsoli
# 3. Pokaż w konsoli ilość elementów krotki
# 4. Pokaż ostatni element krotki wykorzystując len() -1
# 5. Następnie pokaż elementy od drugiego do czwartego
# 6. Pokaż trzeci element od końca z ujemnym indeksem

numbers = (50, 100, 150, 200, 250)
print(type(numbers)) # <class 'tuple'>
print(len(numbers)) # 5
print("Ostatni element krotki:", numbers[len(numbers)-1])
print("Elementy od drugiego do czwartego:", numbers[1:4])
print("Trzeci element od końca:", numbers[-3])