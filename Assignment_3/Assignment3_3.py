def main():
    no1 = int(input("Enter no. of Elements : "))

    list1 = []
    for i in range(no1):
        no2 = int(input("Enter a number: "))

        list1.append(no2)
    print("Input Elements : ", list1)


    minimum_result = list1[0]
    for i in list1:
        if i < minimum_result:
            minimum_result = i
    print("The Minimum number : ", minimum_result)

if __name__ == "__main__":
    main()
