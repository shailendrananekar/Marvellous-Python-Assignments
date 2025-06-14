import schedule
import time
import os
import datetime


def BackUp(filename="ABC.txt", logfileName="backup_logger.log"):
    flag1 = os.path.exists(filename)
    if flag1 == False:
        print("The path is invalid!")
        exit()
    print("File exist in current Directory.")

    abcFileContent = open(filename, "r")
    abcData = abcFileContent.read()
    print(f"File Content of {filename}:\n", abcData)

    timestamp = time.ctime()

    bkpfile = filename.replace(".txt", "")
    bkpfile = bkpfile + "_%s.txt" % (timestamp)
    bkpfile = bkpfile.replace(" ", "_")
    bkpfile = bkpfile.replace(":", "")

    bkpobj = open("bkp_" + bkpfile, "w")
    bkpobj.write(abcData)

    flag2 = os.path.exists(logfileName)
    if flag2 == False:
        logfile = open(logfileName, "w")
        logfile.close()
    logfile = open(logfileName, "a")
    print("logging entry at  :", datetime.datetime.now(), "\n")
    logfile.write("logging entry at :" + str(datetime.datetime.now()) + "\n")

    abcFileContent.close()
    logfile.close()
    bkpobj.close()


def main():
    schedule.every(1).minute.do(BackUp)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
