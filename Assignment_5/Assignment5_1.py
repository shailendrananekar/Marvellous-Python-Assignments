def Sum(a, b):
    result = a + b
    print("Sum : ", result)


def Difference(a, b):
    result = a - b
    print("Difference :", result)


def Product(a, b):
    result = a * b
    print("Product :", result)


def Division(a, b):
    if b != 0:
        result = float(a / b)
        print("Division :", result)
    else:
        print("Division by zero is not allowed.")


def main():
    no1 = int(input("Enter the first number: "))
    no2 = int(input("Enter the second number: "))

    Sum(no1, no2)
    Difference(no1, no2)
    Product(no1, no2)
    Division(no1, no2)


if __name__ == "__main__":
    main()
