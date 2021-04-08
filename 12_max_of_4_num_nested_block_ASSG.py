a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a>b:
    if a>c:
        if a>d:
            print(f"max is {a}")
if b>c:
    if b>a:
        if b>d:
            print(f"max is {b}")

if c>a:
    if c>b:
        if c>d:
            print(f"max is {c}")

if d>a:
    if d>b:
        if d>c:
            print(f"max is {d}")