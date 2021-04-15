def get_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i

    return fact


def is_strong(n):
    i = n
    sum = 0
    while i > 0:
        rem = i % 10
        sum += get_factorial(rem)
        i //= 10 # same as i = i // 10

    return n == sum


def main():
    n = int(input("Enter n: "))
    print(f" {n} is a stong number :: {is_strong(n)} ")

main()


"""
Strong number is a special number whose sum of factorial of digits
is equal to the original number.
For example: 145 is strong number. Since, 1! + 4! + 5! = 145
"""