# R147. Prosty odczyt z pliku

fh = open("test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)