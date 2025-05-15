def main():
    no1 = int(input("Enter a number: "))
    count = no1
    for i in range(no1):
        for j in range(count):
            print("*", end=" ")
        print()
        count = count - 1


if __name__ == "__main__":
    main()
