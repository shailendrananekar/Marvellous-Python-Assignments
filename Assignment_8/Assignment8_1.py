import threading
import time


def DisplayEven(no):
    print("Even numbers:", end=" ")
    i = 1
    count = 0
    while count < no:
        if i % 2 == 0:
            print(i, end=" ")
            count = count + 1
        i = i + 1
    print()


def DisplayOdd(no):
    print("odd numbers:", end=" ")
    i = 1
    count = 0
    while count < no:
        if i % 2 != 0:
            print(i, end=" ")
            count = count + 1
        i = i + 1
    print()


def main():
    print("Execution of Parallel")
    start_time = time.time()
    even = threading.Thread(target=DisplayEven, args=(10,))
    odd = threading.Thread(target=DisplayOdd, args=(10,))
    even.start()
    odd.start()
    even.join()
    odd.join()
    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("End of main")


if __name__ == "__main__":
    main()
