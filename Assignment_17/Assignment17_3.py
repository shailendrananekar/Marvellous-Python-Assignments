import schedule
import time


def MySchedule():
    print("Do Coding..!")


def main():
    schedule.every(30).minutes.do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
