import sys
import time


def main():
    timestamp = time.ctime()

    filename = "MarvellousLog%s.log" % (timestamp)
    filename = filename.replace(" ", "_")
    filename = filename.replace(":", "")
    
    fobj = open(filename, "w")

    Border = "-" * 45
    fobj.write("\n" + Border + "\n")
    fobj.write("This is log file of Marvellous Automation script")
    fobj.write("\n" + Border + "\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write("\n" + Border + "\n")
    fobj.write("This is created at")
    fobj.write("\n" + timestamp)
    fobj.write("\n" + Border + "\n")


if __name__ == "__main__":
    main()
