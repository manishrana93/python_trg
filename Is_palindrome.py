def get_reverse(n):
    i = n
    rev = 0

    while i > 0:
        rem = i % 10
        rev = rev * 10 + rem
        i = i // 10

    return rev


def is_palindrome(n):
    return n == get_reverse(n)


def main():
    print(f"2552 <--> {is_palindrome(2552)} ")
    print(f"7799 <--> {is_palindrome(7799)} ")


main()
