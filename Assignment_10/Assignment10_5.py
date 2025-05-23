from functools import reduce


def fun1(i):
    if i <= 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
        j = j + 1
    return True


def fun2(i):

    return i * 2


def func3(x, y):
    if x > y:
        return x
    else:
        return y



def main():
    lst = input("Enter a list of numbers separated by spaces: ")
    lst = lst.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    print("Input List = ", lst)

    print("Data Type = ", type(lst))
    filter_result = list(filter(fun1, lst))
    print("List after filter = ", filter_result)

    map_result = list(map(fun2, filter_result))
    print("List after map = ", map_result)

    reduce_result = reduce(func3, map_result)
    print("Output of reduce = ", reduce_result)


if __name__ == "__main__":
    main()
