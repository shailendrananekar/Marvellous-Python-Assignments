class Book:

    def __init__(self, a):
        self.__price = a

    def setprice(self, p):
        self.__price = p
        return self.__price

    def getprice(self):
        return self.__price


def main():
    book1 = Book(500)

    print("Price of the book is: ", book1.getprice())

    book1.setprice(600)

    print("Updated price of the book is: ", book1.getprice())


if __name__ == "__main__":
    main()
