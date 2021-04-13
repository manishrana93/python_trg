def print_star_triangle(n):
    for i in range(n):
        print("*", end = " ")
    print()


def main():
    for i in range(1//5,0,-1):
        print_star_triangle(i -2) 

main()