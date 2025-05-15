from Arithmetic import Add, Sub, Mult, Div

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    Add(no1, no2)
    print("Addition is: ", Add(no1, no2))

    Sub(no1, no2)
    print("Subtraction is: ", Sub(no1, no2))

    Mult(no1, no2)
    print("Multiplication is: ", Mult(no1, no2))

    Div(no1, no2)
    print("Division is: ", Div(no1, no2))


if __name__ == "__main__":
    main()