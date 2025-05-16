def main():
    num = int(input("Enter a number: "))

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return False
    print(f"{num} is a prime number")
    return True


if __name__ == "__main__":
    main()
