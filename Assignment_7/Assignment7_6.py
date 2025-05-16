def CheckPrime(Value):

    if Value <= 1:
        return False

    for i in range(2, Value):
        if Value % i == 0:
            return False
    return True


def main():
    num = input("Enter list: ")
    lst = []
    lst = num.split(" ")

    lst1 = list()
    for i in range(len(lst)):
        lst1.append(int(lst[i]))

    Fdata = list(filter(CheckPrime, lst1))
    print(f"Prime numbers: {Fdata}", end=" ")


if __name__ == "__main__":
    main()
