import os
import sys
import time
import hashlib
import schedule
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class DuplicateFileRemovalUtils:
    scannedFiles = 0
    deletedFiles = 0
    startingTime = 0

    def __init__(self):
        pass


def CalculateChecksum(path, BlockSize=1024):
    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if flag == False:
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}
    DuplicateFileRemovalUtils.startingTime = datetime.datetime.now()
    cnt = 0
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateChecksum(fname)
            cnt = cnt + 1
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    DuplicateFileRemovalUtils.scannedFiles = cnt
    # print("Total number of files scanned are : ", len(Duplicate))
    return Duplicate


def LogFile_Versions(contentLog, LoggerFiles="Marvellous"):

    flag1 = os.path.exists(LoggerFiles)
    if flag1 == False:
        os.mkdir(LoggerFiles)

    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "_")
    logfileName = os.path.join(LoggerFiles, filename)
    flag2 = os.path.exists(logfileName)
    if flag2 == False:
        logfile = open(logfileName, "w")
        logfile.close()
    logfile = open(logfileName, "a")

    for log in contentLog:
        logfile.write(log + "\n")
    print("Log file created with name : ", filename)

    logfile.close()

    SendEmail(LoggerFiles, filename)


def SendEmail(LoggerFiles, fileAttachment):
    sender_email = "nanekarshailendra@gmail.com"
    receiver_email = sys.argv[3]
    password = "qiuj qygu crwu irub"
    subject = "Duplicate file removal utility log"
    body = (
        "Hi, "
        "\n\nplease find the attached Log file."
        "\n\nThis file contains the details of deleted duplicate files."
        "\n\n"
        + "Starting time of scanning : "
        + str(DuplicateFileRemovalUtils.startingTime)
        + ""
        "\n\n"
        + "Total number of files scanned : "
        + str(DuplicateFileRemovalUtils.scannedFiles)
        + ""
        "\n\n"
        + "Total number of duplicate file found : "
        + str(DuplicateFileRemovalUtils.deletedFiles)
        + ""
        "\n\nRegards,\nMarvellous Infosystems"
        "\nAutomation Team"
        "\n\nNote: This is an automated email, please do not reply."
        "\n\nThank you for using our service."
    )

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))
    logfilepath = os.path.join(LoggerFiles, fileAttachment)
    attachment = open(logfilepath, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition", 'attachment; filename= "%s"' % fileAttachment
    )
    msg.attach(part)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def DeleteDuplicate(Path):

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    Cnt = 0
    logs = []
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if Count > 1:

                logs.append(
                    "Deleted file : " + str(datetime.datetime.now()) + " - " + subvalue
                )
                # print("Deleted file : ", subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0
    DuplicateFileRemovalUtils.deletedFiles = Cnt
    LogFile_Versions(logs)
    # print("Total deleted file : ", Cnt)


def main():
    Border = "-" * 54
    print(Border)
    print("--------------- Marvellous Automation ----------------")
    print(Border)

    if len(sys.argv) == 2:
        if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory timeinterval emailid")
            print("Please provide valid absolute path")

    if len(sys.argv) == 4:
        schedule.every(int(sys.argv[2])).minutes.do(DeleteDuplicate, sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)


if __name__ == "__main__":
    main()
