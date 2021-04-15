def is_perfect(n):
    i = 1
    sum = 0
    while i < n:
        if n % i == 0:
            sum += i
        i += 1

    return n == sum


def main():
    n = int(input("Enter n: "))
    print(f" {n} Perfect number:: {is_perfect(n)} ")
    

main()


"""
In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. For instance, 6 has divisors 1, 2 and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.

"""