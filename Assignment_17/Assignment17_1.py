import schedule
import time

def MySchedule():
    print("Jay Ganesh...")


def main():
    schedule.every(2).seconds.do(MySchedule)

    while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ == "__main__":
    main()
