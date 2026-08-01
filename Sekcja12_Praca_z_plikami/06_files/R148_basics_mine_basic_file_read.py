# R147. Prosty odczyt z pliku
# R148. Ścieżki do plików absolutne i relatywne


# ścieżka relatywna
fh = open("data/output/test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)


# ścieżka absolutna
fh = open("/home/jaro/dev/learning/lab-py3-wasikowski/data/output/test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
