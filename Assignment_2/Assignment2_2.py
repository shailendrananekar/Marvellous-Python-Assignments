def main():
    no1 = int(input("Enter a number: "))

    for i in range(no1):
        for j in range(no1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    main()
