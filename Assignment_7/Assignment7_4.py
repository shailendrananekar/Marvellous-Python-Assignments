from functools import reduce


def Product(A, B):
    return A * B


def main():
    num = input("Enter list: ")
    lst = []
    lst = num.split(" ")

    lst1 = list()
    for i in range(len(lst)):
        lst1.append(int(lst[i]))

    Rdata = reduce(Product, lst1)
    print(f"Product: {Rdata}", end=" ")


if __name__ == "__main__":
    main()
