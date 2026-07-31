# Obsługa plików – odczyt i zapis danych w Pythonie

## ✅ 1. Otwieranie plików
```python
fh = open("nazwa_pliku.txt", "tryb")
```
- Zwraca uchwyt do pliku, który można wykorzystać do operacji (np. odczyt/zapis).

## ✅ 2. Tryby otwierania plików

| Tryb           | Opis                                                     |
|----------------|----------------------------------------------------------|
| `"r"`          | Odczyt (read). Błąd, jeśli plik nie istnieje.            |
| `"w"`          | Zapis (write). Tworzy nowy plik lub nadpisuje istniejący.|
| `"a"`          | Dopisywanie (append). Dodaje dane na końcu pliku.        |
| `"r+"`         | Odczyt i zapis, bez kasowania zawartości.                |
| `"w+"`         | Zapis i odczyt. Kasuje zawartość pliku przy otwarciu.    |
| `"a+"`         | Dopisywanie i odczyt. Zapis dodawany na końcu.           |
| `"rb"` / `"wb"`| Operacje binarne (odczyt/zapis).                         |

## ✅ 3. Przykład: Zapis do pliku
```python
fh = open("test.txt", "w")
fh.write("To jest test.\n")
fh.write("Druga linia.")
fh.close()
```

## ✅ 4. Przykład: Odczyt z pliku
```python
fh = open("test.txt", "r")
content = fh.read()
print(content)
fh.close()
```

## ✅ 5. Wygodne otwieranie plików – `with`
```python
with open("test.txt", "r") as fh:
    for line in fh:
        print(line.strip())
```

## ✅ 6. Operacje na plikach – metody

| Metoda              | Opis                                       |
|---------------------|--------------------------------------------|
| `read()`            | Odczytuje cały plik jako jeden ciąg znaków.|
| `readline()`        | Czyta jedną linię z pliku.                 |
| `readlines()`       | Zwraca listę wszystkich linii.             |
| `write()`           | Zapisuje dane do pliku (ciąg znaków).      |
| `writelines(lista)` | Zapisuje listę ciągów znaków do pliku.     |

## ✅ 7. Ścieżki do plików
```python
fh = open("dane/test.txt", "r")  # relatywna
fh = open("C:/Users/Kuba/Desktop/python/test.txt", "r")  # absolutna
```

## ✅ 8. Sprawdzanie ścieżek – `os`
```python
import os

print("Aktualna ścieżka pliku:", __file__)
print("Folder skryptu:", os.path.dirname(__file__))
print("Bieżący katalog roboczy:", os.getcwd())
```

## ✅ 9. Przykład – zapis do pliku relatywnego
```python
try:
    with open("file1.txt", "w") as fh:
        fh.write("content")
except:
    print("Wystąpił błąd wejścia/wyjścia.")
```

## ✅ 10. Wylistowanie plików w folderze – `os.listdir()`
```python
import os

print(os.listdir("."))
print(os.listdir("./basics"))
print(os.listdir(".."))
print(os.listdir("../programs"))
```

## ✅ 11. Sprawdzanie istnienia pliku
```python
import os

if os.path.exists("test.txt"):
    print("Plik istnieje.")
else:
    print("Plik nie istnieje.")
```

## ✅ 12. Obsługa wyjątków przy operacjach na plikach
```python
try:
    with open("plik.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie został znaleziony.")
except IOError:
    print("Błąd wejścia/wyjścia.")
```

## ✅ 13. Odczyt pliku linia po linii
```python
with open("plik.txt", "r") as f:
    for line in f:
        print(line.strip())
```

## ✅ 14. Praca z plikami binarnymi
```python
with open("image.png", "rb") as f:
    data = f.read()
```

## ✅ 15. Uwaga na kodowanie znaków
```python
with open("plik.txt", "r", encoding="utf-8") as f:
    print(f.read())
```
