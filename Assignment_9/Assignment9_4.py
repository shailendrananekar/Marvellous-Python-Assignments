import threading
import multiprocessing
import time


def normal_fun():
    sum = 0
    for i in range(10000000):
        sum = sum + i
    print("Normal Fun: ", sum)


def threading_fun():
    sum = 0
    for i in range(10000000):
        sum = sum + i
    print("Threading Fun: ", sum)


def multiprocessing_fun():
    sum = 0
    for i in range(10000000):
        sum = sum + i
    print("Microprocessing Fun: ", sum)


def main():

    normal_start_time = time.time()
    N1 = normal_fun()
    normal_end_time = time.time()
    print("Time of normal execution : ", normal_end_time - normal_start_time)
    print()
    threading_start_time = time.time()
    T1 = threading.Thread(target=threading_fun)
    T1.start()
    print("Thread Name:", T1.name)
    print("Thread ID:", T1.ident)
    T1.join()
    threading_end_time = time.time()
    print("Time of Threading execution : ", threading_end_time - threading_start_time)
    print()
    multiprocessing_start_time = time.time()
    P1 = multiprocessing.Process(target=multiprocessing_fun)
    P1.start()
    print("Process Name:", P1.name)
    print("Process ID:", P1.pid)
    P1.join()
    multiprocessing_end_time = time.time()
    print(
        "Time of Multiprocessing execution : ",
        multiprocessing_end_time - multiprocessing_start_time,
    )
    print()
    print("exit from main")


if __name__ == "__main__":
    main()
