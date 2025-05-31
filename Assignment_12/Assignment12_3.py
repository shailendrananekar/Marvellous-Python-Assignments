class Arithmetic:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def Accept(self):
        self.a = float(input("Enter first number: "))
        self.b = float(input("Enter second number: "))

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b


def main():

    arithmetic = Arithmetic()

    arithmetic.Accept()

    print(f"Addition: {arithmetic.add()}")
    print(f"Subtraction: {arithmetic.subtract()}")
    print(f"Multiplication: {arithmetic.multiply()}")
    print(f"Division: {arithmetic.divide()}")

if __name__ == "__main__":
    main()
