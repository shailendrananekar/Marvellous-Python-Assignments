def main():
    numbers = input("Input 2 numbers for multiplication (with space)  : ")
    no = numbers.split()
    if len(no) != 2:
        print("Please enter exactly two numbers.")
        return
    else:
        x = int(no[0])
        y = int(no[1])

    mult = lambda x, y: x * y

    print("output : ", mult(x, y))


if __name__ == "__main__":
    main()
