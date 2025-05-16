def Increase(Value):
    return Value * 2


def main():
    num = input("Enter list: ")
    lst = []
    lst = num.split(" ")

    lst1 = list()
    for i in range(len(lst)):
        lst1.append(int(lst[i]))

    Mdata = list(map(Increase, lst1))
    print(f"Doubled list: {Mdata}", end=" ")


if __name__ == "__main__":
    main()
