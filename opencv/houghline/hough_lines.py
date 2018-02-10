#!/usr/bin/python2
#-*-coding:utf8-*-
import cv2
import numpy as np
def detect_lines(cnt):
	img = cv2.imread('input.jpeg')
	cnt = cv2.getTrackbarPos('cnt', 'image')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,200)
	lines = cv2.HoughLines(edges,1,np.pi/180,cnt)
	lines1 = lines[:,0,:]#提取为为二维
	print lines1.shape
	for rho,theta in lines1[:]: 
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a)) 
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
	cv2.imshow("image", cv2.pyrDown(cv2.pyrDown(img)))
img = cv2.imread('input.jpeg') 
cnt = 100
cv2.namedWindow('image')
cv2.createTrackbar('cnt', 'image', cnt, 200, detect_lines)
detect_lines(0)
if cv2.waitKey(0) == 27:
	cv2.destroyAllWindows()
