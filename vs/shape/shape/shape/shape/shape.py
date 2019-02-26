import numpy
import imutils
import cv2
import time

start = time.time() * 1000

img = cv2.imread('./shapes.png', 1)
minRGB = numpy.array([0, 0, 0])
maxRGB = numpy.array([20, 20, 20])
print(img)
imageMask = cv2.inRange(img, minRGB, maxRGB)

contours = cv2.findContours(imageMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

numberOfContours = len(contours)

drawShapeColor = [0, 255, 0]
for i in contours:
	cv2.drawContours(img, [i], -1, drawShapeColor, 4)

print(numberOfContours, 'shapes were found')
cv2.imshow("Loaded image", img)
cv2.imshow("Mask of image", imageMask)

print("Execution time", time.time() * 1000 - start)

cv2.waitKey(0)
