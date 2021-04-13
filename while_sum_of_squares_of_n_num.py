def sum_nat(n):
    s = 0
    i=1
    while (i<=n):
        s = s + i*i
        i=i+1

    return s


def main():
    n = int((input("Enter n: ")))
    sum = sum_nat(n)
    print(f"Sum of first {n} Natural numbers = {sum}")


main()