def get_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact

def main():
    n = int(input("Enter n: "))
    factorial = get_factorial(n)
    print(f"factorial of {n} is {factorial} ")

main()