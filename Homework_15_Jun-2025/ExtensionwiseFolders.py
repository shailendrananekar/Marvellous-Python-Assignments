import os
import sys
import time
import shutil


def movetoFolder(file, folderName):

    flag1 = os.path.exists(folderName)
    if flag1 == False:
        os.mkdir(folderName)

    shutil.move(file, folderName)
    print(f"{file} : file moved to folder : {folderName}")


def CreateFolderExtensionWise(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if flag == False:
        print("The path is invalid !")
        exit()

    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid But the Target is not Directory ")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            extension = fname.split(".")
            movetoFolder(fname, extension[1])
            # print("File name is : ", fname)


def main():

    Border = "-" * 45
    print(Border)
    print("----------Marvellous Automation--------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Application is used to perform directory cleaning")
            print("This directory Automation script")
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the given script as : ")
            print("ScriptName.py NameofDirectory")
            print("Please provide valid absolute path")
        else:
            CreateFolderExtensionWise(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the flags as : ")
        print("--h : used to display the help")
        print("--u : used to display the usage")

    print(Border)
    print("------Thank You for using our script---------")
    print("----------Marvellous Infosystem--------------")
    print(Border)


if __name__ == "__main__":
    main()
