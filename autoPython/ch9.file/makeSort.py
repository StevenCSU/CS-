# makeSort.py - find all the file under the folder with same
#               prefix and check if there is missing number
#               (spam001.txt, spam003.txt)
# filename.startswith()
# shutil.move()

import os, shutil

def findMissing(folder, prefix):
    folder = os.path.abspath(folder)

    # get the filenames under the directory
    fileList = os.listdir(folder)
    # check if the file has the prefix
    fileNames = [x for x in fileList if x.startswith(prefix)]
    fileNames = sorted(fileNames)
    print(fileNames)
    # change the name if necessary
    start = 1
    for file in fileNames:
        # start += 1
        oldName, suffix = file.split('.')
        num = int(oldName.split(prefix)[1])
        while True:
            if num == start:
                break
            print('Missing num: ' + str(start))
            start += 1
        # num = start
        # newFile = prefix + str(num) + '.' + suffix
        # shutil.move(os.path.join(folder,file),
        #     os.path.join(folder,newFile))
        start += 1
    
    n = 1 
    for file in fileNames:
        suffix = file.split('.')[1]
        newFile = prefix + ('%03d' % n) + '.' + suffix
        print(newFile)
        shutil.move(os.path.join(folder, file), os.path.join(folder,newFile))
        n += 1

findMissing('./test', 'a')