def CheckEven(Value):

    return Value % 2 == 0


def main():
    num = input("Enter list: ")
    lst = []
    lst = num.split(" ")

    lst1 = list()
    for i in range(len(lst)):
        lst1.append(int(lst[i]))

    Fdata = list(filter(CheckEven, lst1))
    print(f"Even numbers: {Fdata}", end=" ")


if __name__ == "__main__":
    main()
