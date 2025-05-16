def main():
    A = 1
    B = 100
    sum = 0
    for i in range(A, B + 1):
        if i % 2 == 0:
            sum = sum + i
    print(f"Sum of even numbers between {A} to {B} is: {sum}")


if __name__ == "__main__":
    main()
