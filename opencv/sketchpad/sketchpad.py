#!/usr/bin/python2.7
#-*-coding:utf8-*-
#from http://blog.csdn.net/qxconverse/article/details/60338689
#可以学到的有:
#TraceBar的使用
#用户操作(鼠标键盘)触发函数的方法
import cv2
import numpy as np

drawing = False
mode = 'r'
ix, iy = -1, -1

def nothing(x):
    pass

def draw_circle(event,x,y,flags,param):
    #get value
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    color = (b,g,r)
    s = cv2.getTrackbarPos('eraser','image')
    thin = cv2.getTrackbarPos('thin','image')
    if s == 1:
        color = (255,255,255)

    global ix,iy,drawing,mode
    #case events
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == 'l':
                cv2.line(img, (ix,iy),(x,y),color,thin)
            elif mode == 'r':
                cv2.rectangle(img, (ix,iy),(x,y),color,thin)
            elif mode == 'c' : 
                cv2.circle(img,(x,y),thin,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False
#init--white background,BGR
img = np.zeros((512,512,3), np.uint8)
img[:] = 255
#UI
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('eraser','image',0,1,nothing)
cv2.createTrackbar('thin','image',1,50,nothing)
#ui<-->function
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image',img)
    #ui_behavior
    k = cv2.waitKey(1) & 0xFF
    if k == ord('l'):
        mode = 'l'
    elif k == ord('c'):
        mode = 'c'
    elif k == ord('r'):
        mode = 'r'
    elif k == 27:
        break
