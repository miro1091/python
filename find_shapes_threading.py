import numpy
import imutils
import cv2
import time
import threading

img = None
imageMask = None
contours = None

def loadImage():

    global img
    img = cv2.imread('./shapes.png', 1)

def createShapeMask():

    global imageMask
    minRGB = numpy.array([0, 0, 0])
    maxRGB = numpy.array([20, 20, 20])
    imageMask = cv2.inRange(img, minRGB, maxRGB)


def getContours():

    global contours
    contours = cv2.findContours(imageMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    numberOfContours = len(contours)
    print(numberOfContours, 'shapes were found')

def drawShapeColorToDefaultImg():

    global contours
    drawShapeColor = [0, 255, 0]
    for i in contours:
        cv2.drawContours(img, [i], -1, drawShapeColor, 4)

def showImages():

    global img, imageMask
    cv2.imshow("Loaded default image", img)
    cv2.imshow("Mask of image", imageMask)


start = time.time() * 1000


thread1 = threading.Thread(target=loadImage)
thread2 = threading.Thread(target=createShapeMask)
thread3 = threading.Thread(target=getContours)
thread4 = threading.Thread(target=drawShapeColorToDefaultImg)

thread1.start()
thread1.join()

thread2.start()
thread2.join()

thread3.start()
thread3.join()

thread4.start()
thread4.join()

showImages()
print("Execution time", time.time() * 1000 - start)

cv2.waitKey(0)