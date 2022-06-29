import cv2
import numpy as np
def nothing(x):
    pass
img = np.zeros((500,500,3),np.uint8)#创建一个长款分别为500，500像素的纯色背景
cv2.namedWindow('Slider')#创建一个视窗
cv2.createTrackbar('R','Slider',0,255,nothing)
cv2.createTrackbar('G','Slider',0,255,nothing)
cv2.createTrackbar('B','Slider',0,255,nothing)#分别创建RGB三个滑动条来改变颜色
cv2.createTrackbar('on or off','Slider',0,1,nothing)#创建一个窗口

while(1):
    cv2.imshow('Slider',img)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break
    r=cv2.getTrackbarPos('R','Slider')
    g=cv2.getTrackbarPos('G','Slider')
    b=cv2.getTrackbarPos('B','Slider')
    s=cv2.getTrackbarPos('on or off','Slider')
    if s==0:
        img[:]=0
    else:
        img[:]=[r,b,g]#将颜色通道按照rbg顺序来排列

cv2.destroyAllWindows()
