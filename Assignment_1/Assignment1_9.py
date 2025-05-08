def PrintEvenNumbers():

    num = int(input("Enter a number: "))
    i = 1
    count = 0
    while count < num:
        if i % 2 == 0:
            print(i, end=" ")
            count += 1
        i += 1


if __name__ == "__main__":
    PrintEvenNumbers()
