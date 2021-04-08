a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a<b:
    if a<c:
        if a<d:
            print(f"min is {a}")
if b<c:
    if b<a:
        if b<d:
            print(f"min is {b}")

if c<a:
    if c<b:
        if c<d:
            print(f"min is {c}")

if d<a:
    if d<b:
        if d<c:
            print(f"min is {d}")