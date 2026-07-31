# R78. Definiowanie funkcji

# wykład
a = 2
b = 4

def add_Numbers(num1, num2):
    result = num1 + num2
    return result

c = add_Numbers(a, b)
print(c) # 6

d = add_Numbers(c, 10)
print(d) # 16



def add_Num(a, b):
    return a + b

def sub_Num(num1, num2):
    result = num1 - num2
    return result


value1 = add_Num(10, 5) # 15
value2 = sub_Num(value1, 9) # 6

print(value1) # 15
print(value2) # 6

print(sub_Num(100, add_Num(12, 18))) # 70

# suma koszyka zakupów
def calc_Basket_Value(basketList):
    basketSum = 0
    for key in basketList:
        basketSum += basketList[key]
    return basketSum

shoppingBasket = {
    "smartphone": 1200,
    "TV": 1500,
    "console": 1500
}

print(calc_Basket_Value(shoppingBasket)) # 1200+1500+1500=4200


# część praktyczna wykładu - plik 'basic functions.py'

def addNumber(a,b):
    return a + b

def subNumber(a,b):
    return a - b

def multiplyNumber(a,b):
    return a * b

def add4numbers(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

print( addNumber(10,5) ) # 15

number = subNumber(100, 56)
print(number) # 44

number = multiplyNumber(33, 4)
print(number) # 132

sum = add4numbers(1, number, addNumber(10, 6), 9 )
print(sum) # 158
