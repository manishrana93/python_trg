def digits(n):
    j=1
    i=0
    while (n//j)>=1:
        i=i+1
        j=j*10
    return i

def main():
    n=int(input("Enter n: "))
    c=digits(n)
    print(c)

main()