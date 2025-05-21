import threading
import time


def DisplayEven(no):
    print("Addition of Even factors:", end=" ")
    factors = []
    factors_sum = 0

    count = 0
    for i in range(1, no):
        if no % i == 0:
            if i % 2 == 0:
                factors.append(i)
                factors_sum = factors_sum + i

    print(factors_sum)


def DisplayOdd(no):
    print("Addition of odd factors:", end=" ")
    factors = []
    factors_sum = 0

    count = 0
    for i in range(1, no):
        if no % i == 0:
            if i % 2 != 0:
                factors.append(i)
                factors_sum = factors_sum + i

    print(factors_sum)


def main():
    print("Execution of Parallel")
    start_time = time.time()
    evenfactor = threading.Thread(target=DisplayEven, args=(10,))
    oddfactor = threading.Thread(target=DisplayOdd, args=(10,))
    evenfactor.start()
    oddfactor.start()
    evenfactor.join()
    oddfactor.join()
    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
