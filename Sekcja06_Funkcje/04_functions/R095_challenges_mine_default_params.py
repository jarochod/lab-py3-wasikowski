# R95. Domyślne argumenty funkcji - zadanie
#
# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami:
#    - email
#    - country z domyślną wartością "Polska"
#    - company z domyślną wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry 
# 3) Przetestuj funkcję z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com będąca z UK


def getEmployee(email, country = "Polska", company = "Example Ltd"):
    return {
        "email": email,
        "country": country,
        "company": company
    }

print( getEmployee("ola@example.com") ) # {'email': 'ola@example.com', 'country': 'Polska', 'company': 'Example Ltd'}
print( getEmployee("kasia@example.com", "UK") ) # {'email': 'kasia@example.com', 'country': 'UK', 'company': 'Example Ltd'}
print( getEmployee("adam@example.com", "DE", "Test Ltd") ) # {'email': 'adam@example.com', 'country': 'DE', 'company': 'Test Ltd'}
