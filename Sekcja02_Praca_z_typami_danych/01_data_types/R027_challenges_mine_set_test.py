# R27. Set - zadanie

# 1. Stwórz set z unikalnymi wartościami jak:
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomocą funkcji add kolejne elementy:
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkość set
# 4. Wykorzystaj pętlę for aby pokazać elementy w set


nameSet = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}
print(nameSet)

nameSet.add("Olek")
nameSet.add("Basia")
nameSet.add("Kasia")
nameSet.add("Karol")
nameSet.add("Zuza")
nameSet.add("Paulina")

print(nameSet)
print(len(nameSet))

for name in nameSet:
    print(name)