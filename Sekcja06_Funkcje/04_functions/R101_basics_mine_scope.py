# R101. Scope zasięg zmiennych - ćwiczenia

number = 12

def test1():
    print(number) # 12

test1() # 12

def test2():
    number = 100
    print(number) # 100
    if 1 == 1:
        print(number) # 100
        if 2 == 2:
            number = 50
            print(number) # 50
    print(number) # 50


test2() # 100
print(number) # 12

print("\ntest3")
def test3():
    global number
    number = 5
    print("test3" ,number) # 5
    if 1 == 1:
        number = 6
        print("test3", number) # 6

test3()
print("global number after test3():", number) # 6

print("\ntest4")
number = 10
def test4(number):
    print("test4 param:", number) # 33
    number = 20
    print("test4 after change:",  number) # 20

test4(33)
print("global number after test():", number)

print("\ntest5")

number = 10
def foo():
    print("foo() number:", number) # foo() number: 10

def bar():
    number = 9
    print("bar() number:", number) # bar() number: 9
    foo()

bar()
print("global number after foo() bar():", number)


print("\ncheck1 & check2")
number = 10

def check1():
    number = 12
    print("check1() number:", number) # check1() number: 12
    
    def check2():
        print("check2() number:", number) # check2() number: 12
    check2()

check1()
print("global number after check1()", number) # global number after check1() 10


print("\nif test")

if 1 == 1:
    data = 100 # utworzy zmienną globalną

print("data in global scope:", data)

if 2 == 1:
    nexData = 15

# print("nexData in global scope:", nexData) # NameError: name 'nexData' is not defined
