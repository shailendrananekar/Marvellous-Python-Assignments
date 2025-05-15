def main():
    no1 = int(input("Enter a number: "))
    factors = list()
    factors_addition = 0
    for i in range(1, no1):
        if no1 % i == 0:
            factors.append(i)
            factors_addition = factors_addition + i

    print("Factors are", factors)
    print("Addition of Factors ", factors_addition)


if __name__ == "__main__":
    main()
