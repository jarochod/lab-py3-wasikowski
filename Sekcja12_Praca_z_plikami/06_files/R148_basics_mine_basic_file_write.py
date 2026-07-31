# R146. Wstęp do pracy z plikami. Zapis do pliku
# R148. Ścieżki do plików absolutne i relatywne

# Obsługa plików - ścieżki plików mogą być relatywne lub absolutne
# Ścieżka względna inaczej zwana relatywna wskazuje na plik lub folder w aktualnej lokalizacji np. 
# względem folderu gdzie aktualnie wykonywany jest skrypt Pythona. 
# Ścieżka absolutna to pełny adres do pliku np: c:\Users\Kuba\Desktop\python\basics\05 OOP\quiz.py

# Poniższy program tworzy plik file1.txt, czyli używając ścieżki względnej/relatywnej. 
# Gdzie pojawi się plik? W folderze projektu. W tym przypadku w katalogu projektu:  

# d:\Projekty\Projekty_VSC\Python\Python_PL_KW_\

try:
    # ścieżka relatywna
    fh = open("file1.txt", "w")
    fh.write("content") # zapis treści "content" do pliku
    fh.close # zakończenie pracy z plikiem
except:
    print("IOError occured")



# ścieżka relatywna
fh = open("test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

fh2 = open("test.txt", "a")
fh2.write("content3\n")
fh2.close()


# ścieżka absolutna
fh = open("D:\\Projekty\\Projekty_VSC\\Python\\Python_PL_KW_\\test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

fh2 = open("D:\\Projekty\\Projekty_VSC\\Python\\Python_PL_KW_\\test.txt", "a")
fh2.write("content3\n")
fh2.close()

