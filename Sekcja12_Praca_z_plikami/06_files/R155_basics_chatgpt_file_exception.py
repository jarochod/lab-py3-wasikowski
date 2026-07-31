# R155_basics_mine_file_exception.py

# zaktualizowana wersja, bardziej odporna na błędy, z użyciem with open(...) as f: i funkcji os.path.join()
# dla poprawnej obsługi ścieżek.



import os  # import modułu do pracy z systemem operacyjnym (ścieżki, pliki)

# Czasami skrypt jest uruchamiany z innego katalogu niż ten, w którym się znajduje,
# dlatego określamy jego rzeczywistą lokalizację:
script_dir = os.path.dirname(__file__)  # ścieżka katalogu, w którym znajduje się plik skryptu
print(script_dir)  # wyświetlenie tej ścieżki

# Tworzymy bezpieczną ścieżkę do pliku 'test.txt' niezależnie od systemu operacyjnego
file_path = os.path.join(script_dir, "test.txt")

try:
    # Użycie 'with' zapewnia automatyczne zamknięcie pliku nawet w razie błędu
    with open(file_path, "w") as fh:
        fh.write("content")  # zapisujemy dane do pliku
except IOError:
    # Obsługa błędów wejścia/wyjścia (np. brak dostępu, brak miejsca na dysku)
    print("Wystąpił błąd wejścia/wyjścia (IOError)")
else:
    # Jeśli nie wystąpił wyjątek — informujemy, że plik został poprawnie zapisany
    print("Zapisano i zamknięto plik pomyślnie")


# ✅ Zalety nowej wersji:
# with open(...) as fh: automatycznie zamyka plik, nawet jeśli pojawi się wyjątek.
# os.path.join(...) zapewnia poprawną składnię ścieżek na różnych systemach (Windows, Linux, macOS).
# Kod jest bardziej czytelny i idiomatyczny zgodnie z dobrymi praktykami Pythona.


"""
# Wersja z pliku Python+-+PDF.pdf

 import os
 # sometimes script runs in different folder
 # from where it is located
 script_dir = os.path.dirname(__file__)
 print(script_dir) # absolute path to runned script
 fh = None
 try: 
    fh = open(script_dir + "/test.txt", "w")
    fh.write("content")
 except IOError:
    print("IOError occured" )
 else: 
    print("closing file")
    fh.close()

"""