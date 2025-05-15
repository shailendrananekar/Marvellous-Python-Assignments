def main():
    no1 = input("Enter a number: ")

    count = 0
    for i in no1:
        if i.isdigit():
            count = count + 1

    print("The number of digits are : ", count)


if __name__ == "__main__":
    main()
