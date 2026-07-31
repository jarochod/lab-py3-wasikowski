# R141. Moduły instrukcja import oraz from import
# Moduły - instrukcja import
# Im więcej kodu piszemy tym bardziej rośnie potrzeba modularyzacji i organizacji naszego programu, aby 
# łatwiej było kontrolować i odnaleźć się w kodzie źródłowym. Przykładowo każda z klas może być w 
# oddzielnym pliku, a dopiero główny plik importujący poszczególne klasy wykorzysta je w faktycznym 
# programie. Dodatkowo pliki z klasami mogą być użyte w innych programach co oszczędza nam czas.
# Moduł to plik Python, który może mieć funkcje, klasy, zmienne czy korzystający z nich działający kod.

# funkcje w osobnym pliku mathModule.py

def addNumber(a, b):
    return a + b