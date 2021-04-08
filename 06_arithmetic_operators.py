a = 21
b = 7

print(str(a) + " + " + str(b) + " = " + str(a+b)) #addition
print(f"{a} - {b} = {a-b}") #Substraction
print("{} * {} = {}".format(a, b, a*b)) #multiplication
print("{x} / {y} = {div}".format(y=b, x=a, div=a/b)) #Division
print(f"{a} // {b} = {a//b}") #floor divison
print(f"{a} % {b} = {a%b}") #remainder/modulus