phonebook = {}

phonebook["Roy"] = "123-456-7890"
phonebook["Helen"] = "987-654-3210"
phonebook["Charlie"] = "555-555-5555"

name = input("Enter a name to find the phone number: ")

if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}")
else:
    print(f"Sorry, {name} is not in the phonebook.")
