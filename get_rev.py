n = int(input("Enter n:"))

def get_rev(n):
    i = n 
    rev= 0

    while i>0:
        rem= i % 10
        rev = rev*10+ rem
        i = i//10

        return rev

def main():
    print(n)  

main()