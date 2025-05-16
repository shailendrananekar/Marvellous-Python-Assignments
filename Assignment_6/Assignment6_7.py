def main():

    num = input("Enter 5 numbers: ")
    lst = []
    lst = num.split(" ")
    if len(lst) != 5:
        print("Please enter exactly 5 numbers.")
        return
    else:
        maximum = 0
        for i in range(len(lst)):
            if int(lst[i]) > int(maximum):
                maximum = int(lst[i])
    print(f"Maximum number is: {maximum}")


if __name__ == "__main__":
    main()
