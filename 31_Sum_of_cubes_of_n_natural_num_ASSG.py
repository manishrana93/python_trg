def get_cube(n):
    sum = 0
    for i in range(1,n+1,1):
        sum = sum + i**3

    return sum


def main():
    n = int(input("Enter n: "))
    cube = get_cube(n)

    print(f"Sum of Cube of {n} Natural numbers = {cube}")


main()