import multiprocessing
import time


def P1_count(input):
    result = 0
    for i in input:
        result = result + (i * i)
    print("P1: ", result)


def P2_count(input):
    result = 0
    for i in input:
        result = result + (i * i)
    print("P2: ", result)


def P3_count(input):
    result = 0
    for i in input:
        result = result + (i * i)
    print("P3: ", result)


def main():
    numbers = [1, 2, 3, 4, 5]
    start_time = time.time()
    P1 = multiprocessing.Process(target=P1_count, args=(numbers,))
    P2 = multiprocessing.Process(target=P2_count, args=(numbers,))
    P3 = multiprocessing.Process(target=P3_count, args=(numbers,))

    P1.start()
    print("Process Name:", P1.name)
    print("Process ID:", P1.pid)
    P2.start()
    print("Process Name:", P2.name)
    print("Process ID:", P2.pid)
    P3.start()
    print("Process Name:", P3.name)
    print("Process ID:", P3.pid)

    P1.join()
    P2.join()
    P3.join()

    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
