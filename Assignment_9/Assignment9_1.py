import threading
import time


def T1_count(input):

    for i in range(1, input + 1):
        print("T1: ", i)
        time.sleep(1)


def T2_count(input):
    for i in range(1, input + 1):
        print("T2: ", i)
        time.sleep(1)


def T3_count(input):
    for i in range(1, input + 1):
        print("T3: ", i)
        time.sleep(1)


def main():

    start_time = time.time()
    T1 = threading.Thread(target=T1_count, args=(5,))
    T2 = threading.Thread(target=T2_count, args=(5,))
    T3 = threading.Thread(target=T3_count, args=(5,))

    T1.start()
    print("Thread Name:", T1.name)
    print("Thread ID:", T1.ident)
    T2.start()
    print("Thread Name:", T2.name)
    print("Thread ID:", T2.ident)
    T3.start()
    print("Thread Name:", T3.name)
    print("Thread ID:", T3.ident)

    T1.join()
    T2.join()
    T3.join()

    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
