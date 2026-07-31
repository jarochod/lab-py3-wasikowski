# R146. Wstęp do pracy z plikami. Zapis do pliku
# R148. Ścieżki do plików absolutne i relatywne


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