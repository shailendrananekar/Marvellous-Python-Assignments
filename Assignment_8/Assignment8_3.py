import threading
import time


def DisplayEven(no):
    print("Addition of Even numbers:", end=" ")
    factors = []
    factors_sum = 0

    count = 0
    for i in no:
        if i % 2 == 0:
            factors.append(i)
            factors_sum = factors_sum + i

    print(factors_sum)


def DisplayOdd(no):
    print("Addition of odd numbers:", end=" ")
    factors = []
    factors_sum = 0

    count = 0
    for i in no:
        if i % 2 != 0:
            factors.append(i)
            factors_sum = factors_sum + i

    print(factors_sum)


def main():

    size = int(input("Enter no. of Elements:"))
    Data = list()

    for i in range(size):
        no = int(input("Enter the value:"))
        Data.append(no)
    print("Input List :", Data)

    print("Execution of Parallel")
    start_time = time.time()
    evenlist = threading.Thread(target=DisplayEven, args=(Data,))
    oddlist = threading.Thread(target=DisplayOdd, args=(Data,))
    evenlist.start()
    oddlist.start()
    evenlist.join()
    oddlist.join()
    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
