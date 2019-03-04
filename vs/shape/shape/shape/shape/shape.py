import numpy
import imutils
import cv2
import time
import urllib.request

start = time.time()

def url_to_image(url):
	resp = urllib.request.urlopen(url)
	image = numpy.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

img = url_to_image('https://www.pyimagesearch.com/wp-content/uploads/2014/10/finding_shapes_example.png')
print(img)
minRGB = numpy.array([0, 0, 0])
maxRGB = numpy.array([20, 20, 20])
imageMask = cv2.inRange(img, minRGB, maxRGB)

contours = cv2.findContours(imageMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

numberOfContours = len(contours)

drawShapeColor = [0, 255, 0]
for i in contours:
	cv2.drawContours(img, [i], -1, drawShapeColor, 4)

print("Execution time", time.time() - start)

print(numberOfContours, 'shapes were found')
cv2.imshow("Loaded image", img)
cv2.imshow("Mask of image", imageMask)

cv2.waitKey(0)
