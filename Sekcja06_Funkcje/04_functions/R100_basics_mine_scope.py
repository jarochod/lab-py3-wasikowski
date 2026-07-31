# R100. Scope zasięg zmiennych

# 1. zmienne lokalne
# Zmienne lokalne zadeklarowane są np wewnątrz funkcji i tylko tam są dostępne.

print("\n1. zmienne lokalne")
number = 20
def printNumber():
    print(number) # 20 / dostęp do zmiennej globalnej, ponieważ nie matakiej w funkcji
    string = "test" # zadeklarowana zmienna lokalna
    print(string) # test

printNumber()
# id(string) # błąd / brak dostępu do string, bo jest zmienną lokalną funkcji


# 2. zmienne glogalne
# Zmienne posiadają swój zasięg, czyli obszar programu, który ma dostęp do tych zmiennych.
# Zasięg wynika z bloków kodu wprowadzonych dzięki funkcjiom, klasom oraz modułom.
# Uwaga! W Python instrukcje if, pętle, try / except nie definiują zasiegu!
print("\n2. zmienne glogalne")
number = 12 # zmienna globalna
print(number)
if number > 0:
    print(number) # instrukcja if ma dostęp do zmiennej globalnej

def printNum():
    print(number) # funkcja ma dostęp do globalnej zmiennej


# 3. Zmienne lokalne przesłaniające globalne
# Zmienne lokalne o tej samej nazwie co globalne je przesłaniają.
# Podczas wywołania funkcji, gdy potrzebny jest dostęp do zmiennej, Python sprawdza czy przypadkiem
# o tej samej nazwie nie jest zadeklarowana wewnątrz funkcji, taka na pierwszenstwo.
# Jeśli nie jest zadeklarowana wewnątrz funkcji, to zmienna szukana jest stopień wyżej np w globalnych zmiennych.
print("\n3. Zmienne lokalne przesłaniające globalne")
      
number = 20
def printNumber():
    number = 6 # deklaracja zmiennej lokalnej o tej samej nazwie przesłania gloablną
    print("number:", number) # odwolanie po number odnosi się do lokalnej zmiennej

printNumber() # number: 6


# 4. Argumenty przesłaniające globalne
# Podobna sytuacja jest z argumentami o tej samej nazwie jak globalna, również przesłoni globalną.
print("\n4. Argumenty przesłaniające globalne")

string = "Hello"
def printData(string):
    print(2, string) # zmienna jako argument przesłania globalną o tej samej nazwie

print(1, string) # 1 Hello
printData("Test") # 2 Test


# 5. Wywołanie funkcji w funkcji.
# Funkcja printData() przesłania zmienną globalną i wywołuje funkcję showInfo().
# Wywołana funkcja showInfo() odwołująca się do string w praktyce odwołuje się globalnego string,
# a nie przysłonietego printData()
print("\n5. Wywołanie funkcji w funkcji.")

string = "Hello"
def showInfo():
    print(3, string) # Uwaga odwołanie do zmiennej globalnej!

def printData():
    string = "Test" # zmienna lokalna przesłania globalną
    print(2, string)
    showInfo() # wywołanie funkcji showInfo()

print(1, string) # 1 Hello
printData() # 2 Test
            # 3 Hello


# 6. Definicja i wywołanie funkcji w funkcji.
# Inna sytuacja jest, gdy funkcja jest zdefiniowana wewnątrz funkcji. Funkcja bar() odwołująca się do
# firstNum wyświetli 1, bo nie znaleziono definicji takiej zmiennej w bar(), ale znajduje się w funkcji test(),
# której jest częścia.
print("\n6. Definicja i wywołanie funkcji w funkcji.")

firstNum = 9
def test():
    firstNum = 1
    print("test() firstNum:", firstNum)
    def bar():
        print("bar() firstNum:", firstNum)
    bar()
    print("end test()")

print("global fristNum", firstNum) # global fristNum 9
test() # test() firstNum: 1
       # bar() firstNum: 1
       # end test()

# 7. Słowo kluczowe global pozwalające na zmianę zmiennej globalnej.
# Czasem zachodzi potrzeba, aby zmienić wartośc zmiennej globalnej z poziomu funkcji.
# Wymagane jest uzycie słowa kluczowego global, aby nie utworzyć lokalnej zmiennej tylko wskazać,
# że chcemy operować na globalnej zmiennej. Global pozwala zmodyfikować zmienną poza swoim scope.
print("\n7. Słowo kluczowe global pozwalające na zmianę zmiennej globalnej.")

number = 20
def printNumber():
    # nie modyfikuje globalnej tylko tworzy lokalną zmienną!
    number = 33 # nie zmieni globalnej
    print("doNumber():",number)

printNumber() # doNumber(): 33
print("global number", number) # global number 20


number = 20
def printNumber():
    global number # number wskazuje na globalną
    number = 33 # modyfikacja globalnej!
    print("doNumber():",number)

printNumber() # doNumber(): 33
print("global number", number) # global number 33

# 8. Instrukcja if nie definiuje zasięgu, podobnie jak pętle i try / except
# Poniższa globalna string będzie nadpisywana w instrukcji if
print("\n8. Instrukcja if nie definiuje zasięgu, podobnie jak pętle i try / except")

string = "Hello"

if 1 == 1:
    print(1, string) # 1 Hello
    if 2 == 2:
        string = "Test" # zmiana globalnego string
        print(2, string) # 2 Test
        if 3 == 3:
            print(3, string) # 3 Test

print(4, string) # 4 Test

# Podobnie wewnątrz funkcji if nie definiuje zasięgu, odnosi się do string zdefiniowanego
# lokalnie w funkcji

string = "Hello"

def testFunc():
    string = "Local Hi"
    if 1 == 1:
        print(1, string) # 1 Local Hi
        if 2 == 2:
            string = "Test" # zmiana strin wewnątrz funkcji!
            print(2, string) # 2 Test
            if 3 == 3:
                print(3, string) # 3 Test
    print(4, string) # 4 Test

testFunc()
print(5, string) # 5 Hello

# Instrukcja if nie definiuje zasięgu.
# Poniżej if zadeflaruje globalną zmienną data, ale info już nie bo się nie uruchomi.

if 1 == 1:
    data = "some data" # zdefiniowanie zmiennej, tutaj globalnej
print(data) # some data

if 2 == 1:
    info = 10
# print(info) # NameError: name 'info' is not defined