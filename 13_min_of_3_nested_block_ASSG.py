a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a<b:
    if a<c:
        print(f"Min = {a}")
    else:
        print(f"Min = {c}")
else:
    if b < c:
        print(f"Min = {b}")
    else:
        print(f"Min = {c}")