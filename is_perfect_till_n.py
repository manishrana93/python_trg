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
    for i in range(1,n+1):
        if is_perfect(i):
            print(i)
        i = i + 1
    

main()
