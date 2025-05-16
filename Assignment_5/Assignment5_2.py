def main():
    vowel = ["a", "e", "i", "o", "u"]
    char = input("Enter a character: ")
    if char.isalpha() == False:
        print("Please enter a valid character.")
        return
    elif len(char) > 1:
        print("Please enter only one character.")
        return
    elif len(char) == 1:
        char = char.lower()
        if vowel.__contains__(char):
            print(f"'{char}' is a vowel.")
        else:
            print(f"'{char}' is a consonant.")


if __name__ == "__main__":
    main()
