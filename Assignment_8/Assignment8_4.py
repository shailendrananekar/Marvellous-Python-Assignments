import threading
import time


def small_count(input):
    count = 0
    for i in input:
        if i.islower():
            count = count + 1
    print("count of Lower case letters : ", count)


def capital_count(input):
    count = 0
    for i in input:
        if i.isupper():
            count = count + 1
    print("count of Upper case letters : ", count)


def digits_count(input):
    count = 0
    for i in input:
        if i.isdigit():
            count = count + 1
    print("count of Digits : ", count)


def main():

    str = input("Enter a string with lower case, upper case and digits :")

    start_time = time.time()
    small = threading.Thread(target=small_count, args=(str,))
    capital = threading.Thread(target=capital_count, args=(str,))
    digits = threading.Thread(target=digits_count, args=(str,))

    small.start()
    print("Thread Name:", small.name)
    print("Thread ID:", small.ident)
    capital.start()
    print("Thread Name:", capital.name)
    print("Thread ID:", capital.ident)
    digits.start()
    print("Thread Name:", digits.name)
    print("Thread ID:", digits.ident)

    small.join()
    capital.join()
    digits.join()

    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
