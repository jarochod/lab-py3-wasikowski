import os

# # print(os.listdir("."))           # aktualny katalog
# print(os.listdir("./Sekcja01_Wstep"))    # podfolder basics
# # print(os.listdir(".."))          # katalog wyżej
# print(os.listdir("../Python_PL_KW")) # katalog wyżej + programs




with open("test.txt", "r") as fh:
    print(fh)
    for line in fh:
        print(line.strip())




fh = open("test.txt", "r")
content = fh.read()
print(content)
fh.close()

fh = open("test.txt", "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
