# R79. Zwracanie wartości z funkcji return

# Return na końcu funkcji jest opcjionalne, umożliwia wyjscie z funkcji w dowolnym momencie.

def printLista(listData):
    if len(listData) <=3:
        #funkcja kończy działanie jeśli lista ma mniej niz 3 elementy
        return
    
    print(listData)
    # return na końcu jest opcjionalnie, jeśli nie zwracana jest konkretna wartość
    return


printLista(("a","b","c")) # nic sie nie wyświetli
printLista(("a","b","c","d","e")) # ('a', 'b', 'c', 'd', 'e')


def addNumbers(a, b, c):
    return a + b + c

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista!")
        return None
    result = 0
    for v in listData:
        result += v
    return result

print(sumListElements([])) # None
print(sumListElements([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 45

def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)

printList([])
printList([6, 7, 8])