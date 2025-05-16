def main():
    num = int(input("Enter a number: "))

    factorial = 1
    for i in range(num, 0, -1):
        factorial = factorial * i
        i = i + 1
    print(f"Factorial of {num} is: {factorial}")


if __name__ == "__main__":
    main()
