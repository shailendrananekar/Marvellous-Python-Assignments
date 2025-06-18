import psutil  # type: ignore
import os
import time
import schedule
import sys

def CreateLog(FolderName):
    flag1 = os.path.exists(FolderName)
    if flag1 == False:
        os.mkdir(FolderName)

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    logfileName = os.path.join(FolderName, filename)
    flag2 = os.path.exists(logfileName)
    if flag2 == False:
        logfile = open(logfileName, "w")
        logfile.close()
    logfile = open(logfileName, "a")
    Border = "-" * 50
    logfile.write(Border)
    logfile.write("\nMarvellous Infosystem Process Log\n")
    logfile.write("Log file is created at : " + time.ctime() + "\n")
    logfile.write(Border + "\n")

    Data = ProcessScan()
    for content in Data:
        logfile.write("%s \n" % content)
    logfile.close()


def ProcessScan():

    listProcess = []

    for proc in psutil.process_iter():
        try:

            info = proc.as_dict(attrs=["pid", "name", "username"])
            info["vms"] = proc.memory_info().vms / (1024 * 1024)
            listProcess.append(info)
        except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
            pass

    return listProcess


def main():
    CreateLog(sys.argv[1])


if __name__ == "__main__":
    main()
