# R24. Typ Dict - słownik

contacts = {
    "Ola" : "ola@example.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts)) # <class 'dict'>
print(len(contacts))

print(contacts.keys()) # dict_keys(['Ola', 'Daniel', 'Ania', 'Rafał'])
print(contacts.values()) # dict_values(['ola@example.com', 30, 'ania@example.com', 'rafal@example.com'])

print("-------")
for key in contacts:
    print(key, contacts[key])

print("-------")
for key in contacts:
    print(key +" "+str(contacts[key]))

print("-------")
for key, value in contacts.items():
    print(key, value)