name="My namE is AnthoNy."

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace("namE","name"))
print(name.find("is"))
print("Yes, 'Anthony' is present.")
print("Manish" not in name)
print(name[0],name[1])
print(name[10:])
print(name.index(" "))
print(name.rindex(" "))
words=name.split(" ")
print(words)
message="_".join(words)
print(message)