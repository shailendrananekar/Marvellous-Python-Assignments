import threading
import time


def T1_count(input):

    for i in range(1, input + 1, 1):
        print(i, end=" ")
    print()

def T2_count(input):
    for i in range(input, 0, -1):
        print(i, end=" ")
    print()

def main():

    start_time = time.time()
    T1 = threading.Thread(target=T1_count, args=(50,))
    T2 = threading.Thread(target=T2_count, args=(50,))

    T1.start()
    print("Thread Name:", T1.name)
    print("Thread ID:", T1.ident)
    while T1.is_alive():
        print("Thread T1 is still running")
 

    T2.start()
    print("Thread Name:", T2.name)
    print("Thread ID:", T2.ident)

    T1.join()
    T2.join()

    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
