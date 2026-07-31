# R147. Prosty odczyt z pliku

# Aby otworzyć plik trzeba użyć metodę open, przekazać ścieżkę do pliku oraz tryb otwarcia pliku, funkcja 
# zwraca uchwyt do pliku na bazie, którego można wykonywać różne operacje.


# Tryby otwarcia pliku:
#  r - otwarcie pliku tylko do odczytu
#  rb - odczyt pliku w formacie binarnym
#  w - plik otwarty do zapisu, zanim będzie zapis na początku treść pliku jest usuwana
#  a - otwarcie pliku do zapisu, dodanie treści na koniec pliku, czyli treść nie jest kasowana
#  Dodanie + powoduje otwarcie pliku zarówno do odczytu i zapisu np r+ (odczyt i zapis)

fh = open("test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)

# Ścieżki plików - Plik file1.txt pojawił się w aktualnym folderze na którym wykonuje się skrypt Pythona 
# tzw. current working directory. W moim przypadku  d:\Projekty\Projekty_VSC\Python\Python_PL_KW_\