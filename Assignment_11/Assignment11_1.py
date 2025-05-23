i = 1


def Display(no):

    global i
    if i <= no:
        # while i <= no:       # normal Iteration
        print(i, end=" ")
        i = i + 1
        Display(no)  # recursion


def main():
    Display(5)


if __name__ == "__main__":
    main()
