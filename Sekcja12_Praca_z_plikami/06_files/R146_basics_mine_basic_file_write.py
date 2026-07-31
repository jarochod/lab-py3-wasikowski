# R146. Wstęp do pracy z plikami. Zapis do pliku

# Obsługa plików - odczyt plików to podstawowa umiejętność każdego programisty. Pliki konfiguracyjne, 
# tekstowe czy bardziej zaawansowane bazy danych pozwalają na przechowywanie danych dla naszych programów.
# Aby otworzyć plik trzeba użyć metodę open, przekazać ścieżkę do pliku oraz tryb otwarcia pliku, funkcja 
# zwraca uchwyt do pliku na bazie, którego można wykonywać różne operacje.


# Tryby otwarcia pliku:
#  r - otwarcie pliku tylko do odczytu
#  rb - odczyt pliku w formacie binarnym
#  w - plik otwarty do zapisu, zanim będzie zapis na początku treść pliku jest usuwana
#  a - otwarcie pliku do zapisu, dodanie treści na koniec pliku, czyli treść nie jest kasowana
#  Dodanie + powoduje otwarcie pliku zarówno do odczytu i zapisu np r+ (odczyt i zapis)

fh = open("test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()



fh2 = open("test.txt", "a")
fh2.write("content3\n")
fh2.close()

# Ścieżki plików - Plik file1.txt pojawił się w aktualnym folderze na którym wykonuje się skrypt Pythona 
# tzw. current working directory. W moim przypadku  d:\Projekty\Projekty_VSC\Python\Python_PL_KW_\

