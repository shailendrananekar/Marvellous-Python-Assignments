def main():
    no1 = int(input("Enter no. of Elements : "))

    list1 = []
    for i in range(no1):
        no2 = int(input("Enter a number: "))

        list1.append(no2)
    print("Input Elements : ", list1)

    no3 = int(input("Element to search : "))

    search_result = 0
    for i in list1:
        if i == no3:
            search_result = search_result + 1
    print("The Frequency is : ", search_result)


if __name__ == "__main__":
    main()
