count = 0


def sum_n(no):
    global count
    # count = 0
    if no > 0:
        # while no > 0:         # normal Iteration

        count = count + no
        no = no - 1

        sum_n(no)               # recursion
    return count


def main():
    no = int(input("Enter a number: "))
    print("Sum is : ", sum_n(no))


if __name__ == "__main__":
    main()
