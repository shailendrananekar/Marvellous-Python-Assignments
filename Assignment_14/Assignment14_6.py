class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def main():
    calc = Calculator()

    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))

    print(f"Addition: {calc.add(a, b)}")
    print(f"Subtraction: {calc.subtract(a, b)}")
    print(f"Multiplication: {calc.multiply(a, b)}")
    print(f"Division: {calc.divide(a, b)}")


if __name__ == "__main__":
    main()
