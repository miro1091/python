# import the necessary packages
import numpy
import imutils
import cv2
import time

start = time.time() * 1000

image = cv2.imread('./shapes.png')

shapeMask = cv2.inRange(image, numpy.array([0, 0, 0]), numpy.array([20, 20, 20]))

cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print(len(cnts), 'shapes were found')
cv2.imshow("Mask", shapeMask)
cv2.imshow("Image", image)
cv2.waitKey(0)

print("Execution time", time.time() * 1000 - start)
