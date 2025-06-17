import sys


def main():
    fobj = open("MarvellousLog.log", "w")

    Border = "-" * 45
    fobj.write(Border + "\n")
    fobj.write("This is log file of Marvellous Automation script" + "\n")
    fobj.write(Border + "\n")


if __name__ == "__main__":
    main()
