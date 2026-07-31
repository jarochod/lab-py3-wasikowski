# R105. Lambda - zadanie

# Zadanie z lambdą i map
# 1) Stwórz listę names z wartościami: Ola, Ania, Kasia
# 2) z pomocą mapy i lambdy dodaj do każdego imienia tekst " Kowalska"
# 3) Wyświetl nową listę w konsoli
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj
#    w nowej liście tylko te które mają więcej niż 12 znaków
#    Pokaż przefiltrowaną listę w konsoli

names = ["Ola", "Ania", "Kasia"]

fullnamesMap = map(lambda x: x + " Kowalska", names)
fullnames = list(fullnamesMap)
print(fullnames) # ['Ola Kowalska', 'Ania Kowalska', 'Kasia Kowalska']

filteredObj = filter(lambda x: len(x)>12, fullnames)
filtered = list(filteredObj)
print(filtered) # ['Ania Kowalska', 'Kasia Kowalska']


# Kod z kursu udemy
names = ["Ola", "Ania", "Kasia"]

ppl = map(lambda x: x + " Kowalska", names)
ppl = list(ppl)
print(ppl)

filtered = filter(lambda x: len(x) > 12, ppl)
print(list(filtered))
