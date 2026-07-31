# R152. Zapis pliku binarnego serializacja z modułem pickle

# Zapis pliku binarnego z modułem pickle - zapis danych binarnych w postaci  całych obiektów 
# nazywamy serializacją, odczyt takich danych określa się mianem deserializacją.


# Powstały plik jest plikiem binarnym, a nie wyłącznie tekstowym, dlatego dane muszą być
# odczytywane w odpowiedniej kolejności. Programy nie znające naszego formatu pliku wyświetlą
# zazwyczaj nic nie mówiące znaki.

print("\nWykład")

import os
import pickle # do zapisu danych binarnych
script_dir = os.path.dirname(__file__)


myInt = 12345
myString = "Hello World"
myList = ["Ola", "Asia", "Adam"]

# wb - zapis pliku w formacie binarnym
fh = open(script_dir + "/data_.dat", "wb")
pickle.dump(myInt, fh)
pickle.dump(myString, fh)
pickle.dump(myList, fh)
fh.close()

# rb - odczyt pliku w formacie binarnym
fh = open(script_dir + "/data_.dat", "rb")

myInt_r = pickle.load(fh)
myString_r = pickle.load(fh)
myList_r = pickle.load(fh)

print(myInt_r)
print(myString_r)
print(myList_r)

fh.close()

print("\nĆwiczenia")

import os
import pickle

scriptDir = os.path.dirname(__file__)

number = 123456
listData = ["Ania", "Ola", "Kasia", 12345]
strData = "Test ąśćłó"

fh = open(scriptDir + "/data.dat", "wb")
pickle.dump(number, fh)
pickle.dump(listData, fh)
pickle.dump(strData, fh)
fh.close()


fh = open(scriptDir + "/data.dat", "rb")
numberInfo = pickle.load(fh)
listInfo = pickle.load(fh)
strInfo = pickle.load(fh)
fh.close()

print(numberInfo)
print(listInfo)
print(strInfo)



