import numpy
import imutils
import cv2
import time
import threading

image = None
shapeMask = None
cnts = None

def loadImage():

    global image
    image = cv2.imread('./shapes.png')

def createShapeMask():

    global shapeMask
    shapeMask = cv2.inRange(image, numpy.array([0, 0, 0]), numpy.array([20, 20, 20]))


def getContours():

    global cnts
    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    print(len(cnts), 'shapes were found')


start = time.time() * 1000

thread1 = threading.Thread(target=loadImage)
thread2 = threading.Thread(target=createShapeMask)
thread3 = threading.Thread(target=getContours)

thread1.start()
thread1.join()

thread2.start()
thread2.join()

thread3.start()
thread3.join()

cv2.imshow("Mask", shapeMask)

print("Execution time", time.time() * 1000 - start)

cv2.imshow("Image", image)
cv2.waitKey(0)
