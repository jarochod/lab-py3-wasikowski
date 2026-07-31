# R118. Przydatne funkcje do operacji na krotkach

# Krotki w przeciwieństwie do listy są niemutowalne, jakakolwiek jej zmiana utworzy nową krotkę w pamięci


##################--------------------
print('\n----wykład-----\n')

tup1 = (0,1) + (2,3) + (4,)
print(tup1) # (0, 1, 2, 3, 4)
print( type(tup1) ) # <class 'tuple'>

print( (1,2) * 3 ) # (1, 2, 1, 2, 1, 2)
print( 4 in tup1) # True
print( len(tup1) ) # 5

print( tup1[2] ) # 2
print( tup1[2:5]) # (2, 3, 4) / zakres

# Błąd
# tup1[3] = 4 # TypeError: 'tuple' object does not support item assignment
# del tup1[2] # TypeError: 'tuple' object doesn't support item deletion

# iterowanie po elementach krotki
for x in tup1:
    print(x)

print( min(tup1) ) # 0
print( max(tup1) ) # 4

print( tuple( [3,4,5] )) # zmiana listy na krotkę

# Metoda .count(x) w krotkach (tuple) zwraca liczbę wystąpień elementu x w danej krotce.
print(tup1.count(0)) # 1
print(tup1.count(5)) # 0

##################--------------------
print('\n----wykład - ćwiczenia-----\n')

tuple1 = (1,2,3,4) + (5,) + tuple([6,7])
print( type(tuple1) ) # <class 'tuple'>
print( tuple1 ) # (1, 2, 3, 4, 5, 6, 7)

print( (1,2) * 4 ) # (1, 2, 1, 2, 1, 2, 1, 2)

print( 9 in tuple1 ) # False
print( tuple1[1] ) # 2
print( len(tuple1) ) # 7

print( min(tuple1) ) # 1
print( max(tuple1) ) # 7

