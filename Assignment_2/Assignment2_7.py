import sys

def main():
    no1 = int(input("Enter a number: "))

    for i in range(1,no1+1):
        for j in range(1,no1+1):
            print(j, end=" ")
        print()


if __name__ == "__main__":
    main()
