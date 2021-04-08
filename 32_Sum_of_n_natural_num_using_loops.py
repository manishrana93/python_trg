def get_sum(n):
    Sum = 0;
    for i in range(n + 1):
        Sum = Sum + i

    return Sum

def main():
    n = int(input("Enter n: "))
    Sum = get_sum(n)
    print(f"Sum of first {n} natural numbers = {Sum}")

main()

