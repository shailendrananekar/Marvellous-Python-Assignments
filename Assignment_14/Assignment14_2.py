class Rectangle:

    def __init__(self, a, b):
        self.length = a
        self.width = b

    def Area(self):
        result = self.length * self.width
        # print("Area of Rectangle is: ", result)
        return result

    def perimeter(self):
        result = 2 * (self.length + self.width)
        # print("Perimeter of Rectangle is: ", result)
        return result


def main():
    rect1 = Rectangle(10, 5)

    area = rect1.Area()
    perimeter = rect1.perimeter()

    print(f"Area : {area}, Perimeter : {perimeter}")

if __name__ == "__main__":
    main()
