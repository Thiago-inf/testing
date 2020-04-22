import sys
import os
from PIL import Image

def isPathValid(folderpath):
    return os.path.exists(folderpath)


def isJPG(filename):
    return filename[-4:] == '.jpg'


def isEmptyList(anylist):
    return len(anylist) == 0


def grabJPGImageFiles(folderpath):
    everything = os.listdir(folderpath)
    just_JPG_files = []
    for item in everything:
        if os.path.isfile(folderpath+item) and isJPG(item):
            just_JPG_files.append(item)

    return just_JPG_files


def removeFormatFromName(filename):
    return filename[0:-4]


def convertImages(folderpath, nameimages_list, newfolder_path):
    for nameimage in nameimages_list:
        image = Image.open(folderpath + nameimage)
        image.save(newfolder_path + 'PNG_' + removeFormatFromName(nameimage) + '.png')


def createDestinationFolder(folderpath):
    if not isPathValid(folderpath):
        os.mkdir(folderpath)


def main():
    folderJPG = sys.argv[1]
    folderPNG = sys.argv[2]
    if isPathValid(folderJPG):
        jpg_images = grabJPGImageFiles(folderJPG)
        createDestinationFolder(folderPNG)
        convertImages(folderJPG, jpg_images, folderPNG)
    else:
        print("Invalid path! Folder does not exist. Check if you put slash or backslash in the last char")

main()

#adding irrelevant comment to test Git