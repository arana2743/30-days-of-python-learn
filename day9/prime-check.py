def isPrime(num):
    for i in range(2,num):
        if(num%i == 0):
            return True
        else:
            return False
def main():
    num = int(input("Enter a number: "))
    if isPrime(num):
        print("It is a prime number")
    else:
        print("Nope!, It's not prime")

if __name__ == '__main__':
    main()
