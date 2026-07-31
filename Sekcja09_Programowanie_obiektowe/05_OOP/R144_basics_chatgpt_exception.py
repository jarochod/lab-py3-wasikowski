# W nawiązaniu do kodu z pliku R144_basics__exception.py na dole jest kod, 
# którym można wywoływać rózne rodzaje błędów.

import sys

data = ["Ola", "Ania", "Adam", "Kasia"]

print(data[0])

index = 2  # zmieniaj to w testach

try:
    # Test 1: IndexError
    # print(data[10])

    # Test 2: InterruptedError
    # raise InterruptedError("some error!")

    # Test 3: Inny błąd – np. ZeroDivisionError
    a = 1 / 0

except IndexError:
    print("Error IndexError!", sys.exc_info()[0])
except InterruptedError:
    print("Error InterruptedError!", sys.exc_info()[0])
except:
    print("Error!", sys.exc_info()[0])
else:
    print("No error!")

print(data[3])



"""
import sys

data = ["Ola", "Ania", "Adam", "Kasia"]
print(data[0])  # wypisze: Ola

index = 2
try:
    print(data[index])        # wypisze: Adam
    print(data[index - 1])    # wypisze: Ania
    raise InterruptedError("some error!")  # sztucznie wywołany wyjątek
except IndexError:
    print("Error IndexError!", sys.exc_info()[0])
except InterruptedError:
    print("Error InterruptedError!", sys.exc_info()[0])  # zostanie wykonane to
except:
    print("Error!", sys.exc_info()[0])
else:
    print("No error!")  # nie wykona się, bo wystąpił wyjątek

print(data[3])  # wypisze: Kasia

"""






