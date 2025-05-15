from functools import reduce


def main():

    print("Enter no. of Elements:")
    size = int(input())

    Data = list()

    print("Enter the values:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)

    FData = list(filter(lambda X: X % 2 == 0, Data))
    print("Filtered Data is : ", FData)

    MData = list(map(lambda Value: Value * Value, FData))
    print("Mapped Data is : ", MData)

    RData = reduce(lambda A, B: A + B, MData)
    print("Reduced Data is : ", RData)


if __name__ == "__main__":
    main()
