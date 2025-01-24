"""
Dictionary Key Check

Which of these instructions you can use to check if the key "Bob" is present in the "phonebook" dictionary?

- phonebook["Bob"] is not None

- phonebook.Bob != None

- phonebook["Bob"] != None

- phonebook.contains("Bob")

- "Bob" in phonebook
"""

phonebook = {"Bob": 15, "Bubba": 16}

# Answer:
print("Bob" in phonebook)
