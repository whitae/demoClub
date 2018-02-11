#!/usr/bin/python2.7
#-*-cosding:utf8-*-
import cv2
import numpy as np
def detect_lines(cnt):
    img = cv2.imread('input.jpeg')
    cnt = cv2.getTrackbarPos('cnt', 'image')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)
    lines = cv2.HoughLines(edges, 1, np.pi/180, cnt)
    if type(lines) == type(None):
        print "length of lines ==0"
        return
    lines = lines[:,0,:]
    xMax, yMax = edges.shape
    for rho, theta in lines:
        print np.sin(theta)
        if np.sin(theta)>0.5:
            x0, x1 = 0, xMax
            y0 = int((-x0*np.cos(theta) + rho)/np.sin(theta))
            y1 = int((-x1*np.cos(theta) + rho)/np.sin(theta))
        else:
            y0, y1 = 0, yMax
            x0 = int((-y0*np.sin(theta) + rho)/np.cos(theta))
            x1 = int((-y1*np.sin(theta) + rho)/np.cos(theta))
        cv2.line(img, (x0, y0), (x1, y1), (0, 255, 0), 1)
    cv2.imshow('image',cv2.pyrDown(cv2.pyrDown(img)))
img = cv2.imread('input.jpeg')
cnt = 100
cv2.namedWindow('image')
cv2.createTrackbar('cnt', 'image', cnt, 200, detect_lines)
detect_lines(cnt)
while(1):
	if cv2.waitKey(0) == 27:
	    cv2.destroyAllWindows()


