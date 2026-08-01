# R147. Prosty odczyt z pliku

fh = open("data/output/test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
