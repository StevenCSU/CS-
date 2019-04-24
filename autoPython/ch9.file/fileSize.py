# fileSize.py - Find the big file or folder
#               return the abs path of these file/folder

import os


def fileSize(folder, size):
    folder = os.path.abspath(folder)
    size = int(size)
    # generate the filenames in the folder
    for folderName, subfolders, filenames in os.walk(folder):
        if os.path.getsize(folderName) > size:
            print(folderName)
        for filename in filenames:
            filepath = os.path.join(folderName, filename)
            if os.path.getsize(filepath) > size:
                print(filepath)

fileSize('/Users/steven/Downloads', 1024**2)
