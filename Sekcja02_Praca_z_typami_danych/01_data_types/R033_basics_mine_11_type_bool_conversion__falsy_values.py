# R33. Konwersje typów bool

print(bool()) # False - brak przypisanej wartości zwróci domyślnie False

# Falsy values, czyli wartości które dają false przy konwersji na boolean
print( bool(False) ) # False
print( bool(0) ) # False
print( bool(0.0) ) # False
print( bool( () ) ) # False - puste ktotki
print( bool( [] ) ) # False - puste listy
print( bool( {} ) ) # False - puste zbiory
print( bool( '' ) ) # False - pysty łańcuch znaków
print( bool( None ) ) # False - None oznacza brak przypisanej wartości

print( bool(True) ) # True
print( bool(10) ) # True
print( bool(-10) ) # True
print( bool(-12.234) ) # True
print( bool( (1,2,3) ) ) # True - krotki z przynajmiej jednym elementem
print( bool( [0] ) ) # True - listy z przynajmiej jednym elementem
print( bool( {0} ) ) # True - zbiory z przynajmiej jednym elementem
print( bool( "z" ) ) # True - string z przynajmiej jednym znakiem