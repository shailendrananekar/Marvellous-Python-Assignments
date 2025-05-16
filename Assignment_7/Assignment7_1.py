def main():
    num = int(input("Enter a number: "))

    square = lambda x: x * x
    print("Square: ", square(num))

    cube = lambda y: y * y * y
    print("Cube: ", cube(num))


if __name__ == "__main__":
    main()
