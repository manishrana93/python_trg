from _typeshed import StrPath


def is_prime(n):
    start=2
    stop=n-1

    i= start 
    while ( i <= stop):
        if n % i ==0:
            return False
        i = i + 1
    return True

def print_is_prime_status(n):
    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number") 

def main():
    print_is_prime_status(2)
    print_is_prime_status(5)
    print_is_prime_status(7)
    print_is_prime_status(8)

main()   
