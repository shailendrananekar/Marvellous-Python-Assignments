i = 0


def sum(no):

    global i
    if no >= 1:
        # while no >= 1:  # normal Iteration
        i = i + no
        no = no - 1
        sum(no)  # recursion
    return i


def main():
    res = sum(4)
    print("sum:", res)


if __name__ == "__main__":
    main()
