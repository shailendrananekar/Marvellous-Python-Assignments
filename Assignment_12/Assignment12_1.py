class Demo:
    value = 0

    def __init__(self, a, b):
        self.no1 = int(input("Enter first number: "))
        self.no2 = int(input("Enter second number: "))

    def Fun(self):
        print("Value of no1 from Fun() is: ", self.no1)
        print("Value of no2 is from Fun(): ", self.no2)

    def Gun(self):
        print("Value of no1 from Gun() is: ", self.no1)
        print("Value of no2 is from Gun(): ", self.no2)


def main():
    obj1 = Demo(10, 20)
    obj2 = Demo(51, 101)
    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()
