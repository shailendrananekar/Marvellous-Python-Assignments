import multiprocessing
import time


def P1_count(input):
    result = 1
    for i in input:
        result = result * i
    print("Factorial : ", result)


def main():
    numbers = [1, 2, 3, 4, 5]
    start_time = time.time()
    with multiprocessing.Pool(processes=3) as p1:
        p1.map(P1_count, (numbers,))

    p1.join()

    end_time = time.time()
    print("Time required for execution : ", end_time - start_time)

    print("exit from main")


if __name__ == "__main__":
    main()
