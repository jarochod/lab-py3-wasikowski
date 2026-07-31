# R73. Zagnieżdżone petle

# zmodyfikowałem to co w pierwszej częsci wykładu
i=0
while(i < 3):
    strData = str(i)
    j = 0
    while(j<3):
        strData+=" "+str(j)
        j+=1
    print(strData)
    i+=1

# wynik
# 0 0 1 2
# 1 0 1 2
# 2 0 1 2

print ("---for-----")

listsData = [ 
    [0,1,2,3,4],
    ["Ola", "Ala", "Adam"],
    [10,"Adam", 20, "Ania"]
]

for listData in listsData:
    for v in listData:
        print(v)


print ("---while----")
listsData = [ 
    [0,1,2,3,4],
    ["ola","Ala","Adam"],
    [10, "Adam", 20, "Ania"]
]

i = 0
while i < len(listsData):
    j = 0
    while j < len(listsData[i]):
        print(listsData[i][j])
        j += 1
    i += 1