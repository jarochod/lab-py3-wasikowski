## 📂 Obsługa plików w Pythonie

### 1. Podstawy pracy z plikami

#### Otwarcie pliku:

```python
fh = open("test.txt", "w")   # otwarcie pliku do zapisu
fh.write("content")          # zapis treści do pliku
fh.close()                   # zamknięcie pliku
```

#### Tryby otwierania plików:

| Tryb | Opis                               |
|------|------------------------------------|
| `r`  | odczyt (plik musi istnieć)         |
| `rb` | odczyt binarny                     |
| `w`  | zapis (usuwa istniejącą zawartość) |
| `a`  | dopisywanie na końcu pliku         |
| `r+` | odczyt i zapis                     |
| `w+` | zapis i odczyt (czyści plik)       |
| `a+` | dopisanie i odczyt                 |

| Tryb           | Opis                                                     |
|----------------|----------------------------------------------------------|
| `"r"`          | Odczyt (read). Błąd, jeśli plik nie istnieje.            |
| `"w"`          | Zapis (write). Tworzy nowy plik lub nadpisuje istniejący.|
| `"a"`          | Dopisywanie (append). Dodaje dane na końcu pliku.        |
| `"r+"`         | Odczyt i zapis, bez kasowania zawartości.                |
| `"w+"`         | Zapis i odczyt. Kasuje zawartość pliku przy otwarciu.    |
| `"a+"`         | Dopisywanie i odczyt. Zapis dodawany na końcu.           |
| `"rb"` / `"wb"`| Operacje binarne (odczyt/zapis).                         |


---

### 2. Ścieżki do plików

#### Rodzaje ścieżek:
- **Relatywna (względna)** – np. `./folder/plik.txt` – względem katalogu uruchomienia skryptu.
- **Absolutna** – np. `C:/Users/Kuba/Desktop/python/basics/plik.txt`.

#### Przykład użycia ścieżki relatywnej:

```python
try:
    fh = open("file1.txt", "w")
    fh.write("content")
    fh.close()
except:
    print("IOError occurred")
```

---

### 3. Sprawdzanie lokalizacji plików i skryptu

```python
import os

print("__file__: ", __file__)                     # ścieżka do bieżącego skryptu
script_dir = os.path.dirname(__file__)            # folder, w którym znajduje się skrypt
print("script_dir:", script_dir)

print("current working directory:", os.getcwd())  # bieżący katalog uruchomienia skryptu
```

---

### 4. Wylistowanie plików z katalogów

```python
import os

# Pliki w bieżącym folderze
print(os.listdir("."))

# Pliki w podfolderze basics
print(os.listdir("./basics"))

# Pliki w podfolderze basics/05 OOP
print(os.listdir("./basics/05 OOP"))

# Pliki katalog wyżej (np. Desktop)
print(os.listdir(".."))

# Pliki w katalogu ../programs
print(os.listdir("../programs"))
```

---

### 5. Pliki tekstowe z kodowaniem UTF-8 (np. polskie znaki)

#### Zapis:
```python
import os
script_dir = os.path.dirname(__file__)
fh = open(script_dir + "/ogonki.txt", "w", encoding="utf-8")
fh.write("Polskie ogonki ąśćńłę.\n")
fh.write("Kolejne ogonki ęńćśął.")
fh.close()
```

#### Odczyt wszystkich linii:
```python
fh = open(script_dir + "/ogonki.txt", "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
```

#### Odczyt linia po linii:
```python
fh = open(script_dir + "/ogonki.txt", "r", encoding="utf-8")
while True:
    line = fh.readline()
    if not line:
        break
    print(line)
fh.close()
```

---

### 6. Pliki binarne z `pickle` (serializacja)

#### Zapis do pliku binarnego:
```python
import os
import pickle

script_dir = os.path.dirname(__file__)
myInt = 12345
myString = "Hello World!"
myList = ["Ola", "Asia", "Adam"]

fh = open(script_dir + "/data.dat", "wb")
pickle.dump(myInt, fh)
pickle.dump(myString, fh)
pickle.dump(myList, fh)
fh.close()
```

#### Odczyt z pliku binarnego (deserializacja):
```python
import pickle

fh = open(script_dir + "/data.dat", "rb")
myInt = pickle.load(fh)
myString = pickle.load(fh)
myList = pickle.load(fh)
fh.close()

print(myInt, myString, myList)
```

---

## 📝 Wskazówki i dobre praktyki

- **Zawsze zamykaj pliki** po zakończeniu operacji (lepiej używać `with` – zobacz poniżej).
- **Używaj `with` do automatycznego zamykania plików**:
```python
with open("plik.txt", "r", encoding="utf-8") as fh:
    for line in fh:
        print(line)
```
- **Sprawdzaj `os.getcwd()` i `__file__`**, by zrozumieć różnice między katalogiem uruchomienia a lokalizacją skryptu.

---
