# R146. Wstęp do pracy z plikami. Zapis do pliku
# R148. Ścieżki do plików absolutne i relatywne


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
