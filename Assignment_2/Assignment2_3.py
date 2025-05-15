def main():
    no1 = int(input("Enter a number: "))
    factorial_result = 1
    for i in range(1, no1 + 1):
        factorial_result = factorial_result * i
    print("Factorial is", factorial_result)


if __name__ == "__main__":
    main()
