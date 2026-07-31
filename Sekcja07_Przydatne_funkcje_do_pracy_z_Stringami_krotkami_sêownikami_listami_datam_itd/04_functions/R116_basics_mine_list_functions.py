# R116. Przydatne funkcje do operacji na listach

# Praca z listami
##################--------------------
print('\n----wykład-----\n')

list1 = [0,1,2,3,4,5,6]
print( list1[2]) # pobranie elementu: 2
print( list1[2:4]) # pobranie zakresu: [2,3]

list2 = ["Ania", "Ola", "Rafał", "Adam"]
list2[2] = "Daniel" # zmiana elementu listy
print(list2) # ['Ania', 'Ola', 'Daniel', 'Adam']

del list2[1] # skasowanie elementu listy
print(list2) # ['Ania', 'Daniel', 'Adam']

print( len(list2) ) # długośc listy: 3
print( max([4,8,1])) # 8
print( min([4,8,1])) # 1

# zmiana ktotki na listę
print(list( (10,20) )) # [10, 20]

# operator i listy
print( [0,1] + [2,3] )
print( [3,2] * 2 ) # powtórzenie

# sprawdzenie czy element jest w liście
print( 5 in [3,4,5]) # True
print( 0 not in [3,4,5] ) # True

# iterowanie po elementach listy
list3 = ["Ola", "Ania", "Adam"]
for x in list3:
    print(x)


list4 = ["Ania", "Ola"]
list4.append("Ola") # dodanie elemetu do listy
print(list4) # ['Ania', 'Ola', 'Ola']

# ilość powtórzeń
print(list4.count("Ola")) # 2

# dodanie elementów do listy z innej sekwencji
list4.extend(["Rafał", "Kasia"])
print(list4) # ['Ania', 'Ola', 'Ola', 'Rafał', 'Kasia']

print(list4.index("Ola")) # 1 / zwraca najmniejszy index wystąpienia wartości

# umieszczenie elementu pod indeksem, przesuwa istniejący dalej
list4.insert(0, "Kinga")
print(list4) # ['Kinga', 'Ania', 'Ola', 'Ola', 'Rafał', 'Kasia']

list5 = [6,0,1,2]
list5.reverse() # odwrócenie kolejności
print(list5) # [2, 1, 0, 6]

list5.sort() # sortowanie
print(list5) # [0, 1, 2, 6]

# zwraca i zabiera ostatni element z listy
print(list5.pop()) # 6
print(list5) # [0, 1, 2]


##################--------------------
print('\n----wykład - ćwiczenia-----\n')

list1 = [0,1,2,3,4,5]
print(list1[3]) # 3 / wskazany indeks 
print(list1[1:5]) # [1, 2, 3, 4] / zakres indesku 

list1[0] = 9 # zmiana wskazanego indesku
print(list1) # [9, 1, 2, 3, 4, 5]

# kasowanie wskazanego elementu o podanym indeksie
del list1[1]
print(list1) # [9, 2, 3, 4, 5]
print( len(list1) ) # 5 / długość listy
print( max(list1) ) # 9 / maksymalny element listy
print( min(list1) ) # 2 / minimalny element listy

# konwersja krotki na listę(
print( list( ("Ala", "Ola") ) ) # ['Ala', 'Ola']

# połączenie ze sobą kilku list 
print( [0,1,2] + [3,4] ) # [0, 1, 2, 3, 4]  / +  połączenie list
print( [0,1] * 3 ) # [0, 1, 0, 1, 0, 1] / * powtórzenie elementów listy

# sprawdzenie, czy dany element występuje w liście
print( 9 in [0,1] ) # False
print( 9 not in [0,1] ) # True

# appent() dodanie elementu do listy
list1.append(99)
print(list1) # [9, 2, 3, 4, 5, 99]
list1.append(3)
print(list1.count(3)) # 2 / zliczanie ilości wystąpień elementu w liście
print(list1) # [9, 2, 3, 4, 5, 99, 3]
list1.remove(3)  # usuwa pierwszy element 3 z listy
print(list1) # [9, 2, 4, 5, 99, 3]

# rozszeżanie listy o kilka elementów
list1.extend([7,8,9])
print(list1) # [9, 2, 3, 4, 5, 99, 3, 7, 8, 9]

# dodanie pod dany indeks, nową wartość (dodano pod indeksem 3, wartość 9)
list1.insert(3, 9)
print(list1) # [9, 2, 3, 9, 4, 5, 99, 3, 7, 8, 9]

# zwraca indeks (pierwszy od lewej) pod którym jest dana wartość 
print(list1.index(99)) # 6


list1.reverse() # odwracanie kolejności elemnetów listy
print(list1) # [9, 8, 7, 3, 99, 5, 4, 9, 3, 2, 9]

#  sort() - sportowanie elementów listy
list1.sort()
print(list1) # [2, 3, 3, 4, 5, 7, 8, 9, 9, 9, 99]

# pop() - zwraca ostatnią wartość i zdejmują ją z listy
num = list1.pop() # zdjęcie ostatniego elementu listy
print("num", num) # num 99
print(list1) # [2, 3, 3, 4, 5, 7, 8, 9, 9, 9] / list1 nie ma już ostatniego elementu 99