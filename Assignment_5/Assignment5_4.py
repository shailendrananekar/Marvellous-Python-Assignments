def main():
    lst = []
    num = input("Enter three numbers : ")
    lst = num.split(" ")
    if len(lst) != 3:
        print("Please enter exactly three numbers.")
        return
    else:
        if lst[0] > lst[1]:
            temp = lst[0]
        elif lst[1] > lst[2]:
            temp = lst[1]
        else:
            temp = lst[2]
    print("Largest number is : ", temp)


if __name__ == "__main__":
    main()
