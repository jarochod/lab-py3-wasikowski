# Obsługa wyjątków - programy w Python mogą reagować na różne nieprzewidziane błędy, dzięki czemu
# mimo problemów mogą zareagować i kontynuować swoja pracę
# Poniżej wyjątek przerywa działanie programu:
 
# data = ["Ania", "Ola", "Kasia"]
# print(data[2])
# print(data[5])



# Poniżej wyjątek prawidłowo jest obsłużony
import sys
data = ["Ania", "Ola", "Kasia"]
print(data[2]) # Kasia
try:
    print(data[5]) # Error:  <class 'IndexError'>
except:
    print("Error: ", sys.exc_info()[0] ) 
print(data[0]) # Ania


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






