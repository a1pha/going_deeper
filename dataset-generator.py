# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:12:38 2019

@author: Mars
"""

import cv2
import numpy as np
import os
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg


arrayCoords = []
def mouseLocationClick(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("click identified at: " +str([x,y])+ " with " +str(len(arrayCoords)+1)+" coordinates saved")
        arrayCoords.append([x,y]) # horizontal position, then vertical position within an image


def cvWindow(nameOfWindow, imageToShow, keypressBool=False):
    print("----------Displaying: "
          + str(nameOfWindow)
          + "    ----------")
    cv2.namedWindow(nameOfWindow, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(nameOfWindow, mouseLocationClick)
    cv2.imshow(nameOfWindow, imageToShow)
    pressedKey = cv2.waitKey(0)
    cv2.destroyAllWindows()
    if keypressBool:
        return pressedKey
   

def fileNameGenerator():
    listOfFiles = []
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    classDict = {"apple" : 5,
                 "banana" : 4,
                # "instant_noodles" : 8,
         #        "potato" : 6,
             #    "water_bottle" : 10
                 }
    folderName = scriptPath + "\\"
    for eachClass in classDict:
        folderName = scriptPath + "\\" + eachClass + "\\"
        folderName += eachClass + "_"
        for eachBindex in range(1,classDict[eachClass]+1):
            indexedName = folderName + str(eachBindex) + "\\"
            for eachNumber in range(1, 201, 5):
                fileName = indexedName + eachClass + "_" + str(eachBindex) + "_1_" + str(eachNumber) + "_depthcrop.png"
                listOfFiles.append(fileName)
    return listOfFiles


def main():
    listOfFiles = fileNameGenerator()
    count = 0
    for eachFile in listOfFiles:
        print(eachFile)
        fileType = eachFile.split("\\")[-1].split("_")[0]
        fileBindex = eachFile.split("\\")[-1].split(".")[0].split("_")[1]
        fileNum = eachFile.split("\\")[-1].split(".")[0].split("_")[-2]
        outFileName = fileType + fileBindex + "_" + fileNum + ".png"
        try:
            depthImg = cv2.imread(eachFile)
            depthImg = cv2.cvtColor(depthImg.copy(), cv2.COLOR_BGR2GRAY)
            imageCols, imageRows = depthImg.shape[::-1]
            image8b = cv2.normalize(depthImg.copy(),
                                    np.zeros(shape=(imageRows, imageCols)),
                                    0,255,
                                    norm_type = cv2.NORM_MINMAX,
                                    dtype = cv2.CV_8U)
            cv2.imwrite(outFileName,image8b)
            print(outFileName + " has been written")
            count += 1
        except AttributeError:
            print(outFileName + " doesn't exist...")
    print("done, with " + str(count) + " images processed successfully")
#    scriptPath = os.path.dirname(os.path.realpath(__file__))
#    imageFilePath = scriptPath + "\\apple\\apple_1\\apple_1_1_116_depthcrop.png"
#    print(imageFilePath)
    
#    depthImg = cv2.imread(imageFilePath)
#    depthImg = cv2.cvtColor(depthImg.copy(), cv2.COLOR_BGR2GRAY)
#    print("big pixel: " + str(np.amax(depthImg)))
#    imageCols, imageRows = depthImg.shape[::-1]
#    image16b = cv2.normalize(depthImg.copy(),
#                            np.zeros(shape=(imageRows, imageCols)),
#                            0,255,
#                            norm_type = cv2.NORM_MINMAX,
#                            dtype = cv2.CV_8U)
#    try:
#        print(image16b.shape)
#        print("big pixel: " + str(np.amax(image16b)))
#    except:
#        print("failed")
#    cvWindow("Test depth image", image16b)
    
if __name__ == '__main__':
    main()