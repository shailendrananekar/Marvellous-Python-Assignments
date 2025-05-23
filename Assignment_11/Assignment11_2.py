i = 1


def factorial(no):

    global i
    if no >= 1:
        # while no >= 1:  # normal Iteration
        i = i * no
        no = no - 1
        factorial(no)  # recursion
    return i


def main():
    res = factorial(5)
    print("\nFactorial:", res)


if __name__ == "__main__":
    main()
