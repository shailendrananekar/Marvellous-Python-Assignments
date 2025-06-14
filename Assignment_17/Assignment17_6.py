import schedule
import time


def LunchTime():

    print("Lunch Time!")


def WrapUpWork():

    print("Wrap Up Work :")


def main():
    schedule.every().day.at("13:00:00").do(LunchTime)
    schedule.every().day.at("18:00:00").do(WrapUpWork)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
