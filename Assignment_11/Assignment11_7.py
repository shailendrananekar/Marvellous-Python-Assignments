count = 1


def triangle(no):
    global count
    # count = 1
    
    if count <= no:
    # while count <= no:            # normal Iteration
        i=1         
        while i <= count:  
            print("*", end=" ")
            i = i + 1
        print()
        count = count + 1

        triangle(no)                # recursion


def main():
    no = int(input("Enter a number: "))
    triangle(no)
    

if __name__ == "__main__":
    main()
