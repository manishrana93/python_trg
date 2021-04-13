def multiplication_table(n):
    for i in range(1, n+1):
        print(f"{n} * {i} ")


def main():
    print ("-------Multiplication Table-------")
    print_multiplication_table(2)
    print("--------------")
    print_multiplication_table(5)
    print("--------------")
    print_multiplication_table(10)

main()
