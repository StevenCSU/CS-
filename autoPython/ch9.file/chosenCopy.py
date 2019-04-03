# chosenCopy - Copy the specific file(.pdf, .jpg, etc) 
#               to a new folder

import shutil, os

def chosenCopy(folder, suffix):
    folder = os.path.abspath(folder)

    name = suffix[1:]
    # create folder under the folder we search.
    destName = os.path.join(folder, name)
    # create folder under this folder
    # destName = os.path.join(os.path.basename(folder),
    #            name)
    os.makedirs(destName)

    print(os.path.abspath(destName))
    print('Creating %s...' % destName)

    # find the file
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        if foldername == destName:
            continue
        for filename in filenames:
            if filename.endswith(suffix):
                shutil.copy(os.path.join(foldername, filename)
                , destName)

chosenCopy('/Users/steven/Downloads', '.pdf')