import schedule
import time


def EmailUpdate():
    print("Checking Email ...")


def main():
    schedule.every(10).seconds.do(EmailUpdate)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
