# R147. Prosty odczyt z pliku
# R148. Ścieżki do plików absolutne i relatywne


# ścieżka relatywna
fh = open("test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)


# ścieżka absolutna
fh = open("D:\\Projekty\\Projekty_VSC\\Python\\Python_PL_KW_\\test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)