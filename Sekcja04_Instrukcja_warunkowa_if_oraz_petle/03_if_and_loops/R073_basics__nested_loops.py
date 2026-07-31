# R73. Zagnieżdżone petle

# dwie pętle while (drugie while zagnieżdżone)
i=0
while(i < 3):
    strData = ""
    j = 0
    while(j<3):
        strData+=" "+str(j)
        j+=1
    print(strData)
    i+=1

print("-----------")

listsData = [ 
    [0,1,2,3,4],
    ["Ola", "Ala", "Adam"],
    [10,"Adam", 20, "Ania"]
]

for listData in listsData:
    for v in listData:
        print(v)
