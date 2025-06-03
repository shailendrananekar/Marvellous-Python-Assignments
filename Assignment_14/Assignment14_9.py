class Product:

    def __init__(self, a, b):

        self.name = a
        self.price = b

    def __eq__(self, p):

        if self.price == p.price:
            return True
        else:
            return False


def main():
    product1 = Product("Laptop", 50000)
    product2 = Product("Mobile", 60000)

    if product1.__eq__(product2):
        print("Both products have the same price.")
    else:
        print("Products have different prices.")


if __name__ == "__main__":
    main()
