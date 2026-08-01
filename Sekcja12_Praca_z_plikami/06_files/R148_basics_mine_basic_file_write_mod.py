# R146. Wstęp do pracy z plikami. Zapis do pliku
# R148. Ścieżki do plików absolutne i relatywne

# Obsługa plików - ścieżki plików mogą być relatywne lub absolutne
# Ścieżka względna inaczej zwana relatywna wskazuje na plik lub folder w aktualnej lokalizacji np.
# względem folderu gdzie aktualnie wykonywany jest skrypt Pythona.
# Ścieżka absolutna to pełny adres do pliku np: c:\Users\Kuba\Desktop\python\basics\05 OOP\quiz.py

# Poniższy program tworzy plik file1.txt, czyli używając ścieżki względnej/relatywnej.
# Gdzie pojawi się plik? W folderze projektu. W tym przypadku w katalogu projektu:
# /lab-py3-wasikowski/

fh = None
try:
    fh = open("data/output/test.txt", "w")
    fh.write("content")
except:
    print("IOError occured")
finally:
    if fh:
        fh.close()  # Zamknie plik ZAWSZE, nawet po błędzie!


# ścieżka relatywna
fh = open("data/output/test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

fh2 = open("data/output/test.txt", "a")
fh2.write("content3\n")
fh2.close()


# ścieżka absolutna
fh = open("/home/jaro/dev/learning/lab-py3-wasikowski/data/output/test.txt", "w")
fh.write("content1\n")
fh.write("content2\n")
fh.close()

fh2 = open("/home/jaro/dev/learning/lab-py3-wasikowski/data/output/test.txt", "a")
fh2.write("content3\n")
fh2.close()

