# import the necessary packages
import numpy as np
import imutils
import cv2
import time
import threading

image = None
shapeMask = None
cnts = None

class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        # load the image
        global image
        image = cv2.imread('./shapes.png')

        print("End " + self.name + "\n")

class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        # find all the 'black' shapes in the image
        global shapeMask
        lower = np.array([0, 0, 0])
        upper = np.array([15, 15, 15])
        shapeMask = cv2.inRange(image, lower, upper)

        print("End " + self.name + "\n")


class Thread3(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print("Starting " + self.name + "\n")

        # find the contours in the mask
        global cnts
        cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        print("I found {} black shapes".format(len(cnts)))

        print("End " + self.name + "\n")


start = time.time() * 1000

thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")

thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()

cv2.imshow("Mask", shapeMask)

print("Execution time", time.time() * 1000 - start)

for c in cnts:
    # draw the contour and show it
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
