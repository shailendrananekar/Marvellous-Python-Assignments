import schedule
import time
import datetime


def CurrentDateTime():
    print("Current Date Time :", datetime.datetime.now())


def main():
    schedule.every(1).minute.do(CurrentDateTime)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
