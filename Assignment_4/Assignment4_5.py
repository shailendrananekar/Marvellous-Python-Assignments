from functools import reduce


def PrimeNum(no1):

    PrimList = []
    if no1 <= 1:
        print("Not a Prime Number")
        return False
    for i in range(2, no1):
        if no1 % i == 0:
            print("Not a Prime Number")
            return False
    PrimList.append(no1)
    return PrimList


def Multi(Value):
    return Value * 2


def Max(A, B):
    maximum_result = 0
    if A > B:
        maximum_result = A
    else:
        maximum_result = B
    return maximum_result


def main():

    elements = int(input("Enter no. of Elements :"))

    Data = list()

    for i in range(elements):
        no = int(input("Enter the value :"))
        Data.append(no)

    print("Input List :", Data)

    FData = list(filter(lambda no1: [no1] if no1 > 1 and all(no1 % i != 0 for i in range(2, no1)) else print("Not a Prime Number") or False
, Data))
    print("Filtered Data is : ", FData)

    MData = list(map(lambda Value: Value * 2, FData))
    print("Mapped Data is : ", MData)

    RData = reduce(lambda A, B: A if A > B else B, MData)
    print("Reduced Data is : ", RData)


if __name__ == "__main__":
    main()
