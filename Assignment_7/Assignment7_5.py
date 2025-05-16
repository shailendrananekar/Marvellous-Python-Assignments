def main():
    input_str = input("Enter a string: ")

    output_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        output_str = output_str + input_str[i]
    if output_str == input_str:
        print(f"{input_str} is a palindrom.")
    else:
        print(f"{input_str} is not a palindrom.")


if __name__ == "__main__":
    main()
