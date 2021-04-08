age = int(input("Enter age: "))

if age < 5:
    print("Play School")
elif age < 13:
    print("School")
elif age < 25:
    print("College")
elif age < 60:
    print("Professional")
else:
    print("Retired")