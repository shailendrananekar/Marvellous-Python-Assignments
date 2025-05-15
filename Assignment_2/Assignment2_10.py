def main():
    no1 = input("Enter a number: ")

    count = 0
    addition_result = 0
    for i in no1:
        if i.isdigit():
            
            addition_result = addition_result + int(i)

    print("The Addition of digits is : ", addition_result)


if __name__ == "__main__":
    main()
