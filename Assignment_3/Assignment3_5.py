from MarvellousNum import ChkPrime


def ListPrime(inputlist):
    primeList = []
    for i in inputlist:
        if ChkPrime(i):
            primeList.append(i)
    print("The Prime numbers are : ", primeList)
    return primeList


def main():
    no1 = int(input("Enter no. of Elements : "))
    list1 = []
    for i in range(no1):
        no2 = int(input("Enter a number: "))
        list1.append(no2)
    print("Input Elements : ", list1)

    addition_result = 0
    primelst = ListPrime(list1)
    for i in primelst:
        addition_result = addition_result + i
    print("The addition of prime numbers is : ", addition_result)


if __name__ == "__main__":
    main()
