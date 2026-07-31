# R27. Set - zadanie

# 1. Stwórz set z unikalnymi wartościami jak:
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomocą funkcji add kolejne elementy:
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkość set
# 4. Wykorzystaj pętlę for aby pokazać elementy w set

set = { "Ania", "Kasia", "Ola",  "Karol", "Daniel", "Zuza" }
print(set)

set.add("Olek")
set.add("Basia")
set.add("Kasia")
set.add("Karol")
set.add("Zuza")
set.add("Paulina")

print(set)
print(len(set))


for name in set:
    print(name)

