def print_multiplication(n):
    i=1
    while(i<=10):
        print(f"{n}*{i}={n*i}")
        i=i+1

def main():
    print("*******Tables*******")
    print_multiplication(5)
    print("-----")
    print_multiplication(8)
    print("---")
    print_multiplication(12)

main()