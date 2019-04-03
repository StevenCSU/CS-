# searchTxt.py - open all text files under the folder,
# find the lines that match the Regex.
# os.chdir() change path
# os.listdir() return list of filename
# os.path.exists() return True or False
# os.path.isdir()  return True or False
# example:python searchTxt.py <abspath> <regex>
# or python searchTxt.py (leave the pathname and regex to the user)

import os
import re

# input abspath
path = input('Please input the abspath you want to search:\n')
# check if the path exists
if os.path.exists(path):
    # ask for regular expression
    # os.chdir(path)
    name = input('Please input the regex you want to use:\n')
    nameRegex = re.compile(r'' + name)
#    textRegex = re.compile(r'\w+.txt')
    filename = os.listdir(path)
    # check the file is a text file
    for file in filename:
        if file.endswith('.txt'):
            with open(file) as f:
                content = f.readlines()
                # check if the line is ok
                for line in content:
                    if nameRegex.search(line):
                        print(line)
                    else:
                        print('No such line.')
else:
    print('The path does not exist.')
