def main():
    vowel = ["a", "e", "i", "o", "u"]
    char = input("Enter a character: ")

    if vowel.__contains__(char):
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is a consonant.")


if __name__ == "__main__":
    main()
