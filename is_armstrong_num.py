def get_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact


def is_armstrong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += rem*rem*rem
        i //= 10 # same as i = i // 10

    return n == sum


def main():
    n = int(input("Enter n: "))
    print(f" {n} is a stong number :: {is_armstrong(n)} ")

main()

