import schedule
import time


def MySchedule():
    print("Namskar...")


def main():
    schedule.every().day.at("09:45:00").do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
