count = 0


def countZeros(no):
    global count
    # count = 0
    if no > 0:
        # while no > 0:          # normal Iteration
        if no % 10 == 0:
            count = count + 1
        no = no // 10
        countZeros(no)           # recursion
    return count


def main():
    no = int(input("Enter a number: "))
    print("The number of zeros in the number is: ", countZeros(no))


if __name__ == "__main__":
    main()
