import schedule
import time
import datetime
import os


def MySchedule(filename="Marvellous.txt"):
    flag = os.path.exists(filename)
    if flag == False:
        file = open(filename, "w")
        file.close()
    file = open(filename, "a")
    print("Current Time :" + datetime.datetime.now().strftime("%H:%M:%S") + "\n")
    file.write("Current Time :" + datetime.datetime.now().strftime("%H:%M:%S") + "\n")

    file.close()


def main():
    schedule.every(5).minutes.do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
