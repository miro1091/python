import numpy
import imutils
import cv2
import time
import threading
import urllib

img = None
imageMask = None
contours = None

def url_to_image(url):
	resp = urllib.urlopen(url)
	image = numpy.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

def loadImage():

    global img
    img = url_to_image('https://www.pyimagesearch.com/wp-content/uploads/2014/10/finding_shapes_example.png')

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


start = time.time()


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
print("Execution time", time.time() - start)

cv2.waitKey(0)