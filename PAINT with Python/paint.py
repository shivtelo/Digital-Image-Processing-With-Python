import cv2
import numpy as np
import random
flag=0
ix=0
iy=0
colors=[0,0,0]
# mouse callback function
def handle_mouse(event,x,y,flags,param):
    global flag
    global ix
    global iy
    global img
    global colors
    if event == cv2.EVENT_RBUTTONDBLCLK:
        flag=3
        return
    if event == cv2.EVENT_RBUTTONDOWN:
        flag=2
        colors[0]=int(input())
        colors[1]=int(input())
        colors[2]=int(input())
        #colors=[0,0,255-colors[2]]
        flag=0
    if event == cv2.EVENT_LBUTTONDOWN:
        if flag==2 or flag==3:
            return
        ix=x
        iy=y
        cv2.line(img,(ix,iy),(x,y),colors,10)
        cv2.imshow('image',img)
        flag=1
        ix=x
        iy=y
    if event == cv2.EVENT_LBUTTONUP:
        if flag==2 or flag==3:
            return
        flag=0
    if event == cv2.EVENT_MOUSEMOVE:
        if flag==2 or flag==3:
            return
        if flag==1:
            cv2.line(img,(ix,iy),(x,y),colors,10)
            ix=x
            iy=y
            cv2.imshow('image',img)
            
            
img = np.zeros((1000,700,3), np.uint8)
img = img+255
#cv2.imshow('image',img)
cv2.namedWindow('image')
cv2.setMouseCallback('image',handle_mouse)
cv2.imshow('image',img)
while(1 and flag!=3):
    if cv2.waitKey(0):
        break
cv2.destroyAllWindows() 
nm=str(random.randrange(1,1000))+".jpg"
cv2.imwrite( nm, img );
           