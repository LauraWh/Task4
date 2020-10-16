#Task 4 - Adjusting
#Transformation Notes
#Code written by Laura Whelan on 09/10/2020

#==========================================
#This code opens an image, crops out the fourth quadrant 
#and rotates the cropped section by 45 degrees.
#==========================================

#import the necessary packages:
import numpy as np
import cv2
import math as m
from matplotlib import pyplot as plt
from matplotlib import image as image
import easygui

#1. Open image 
I = cv2.imread("wartime.jpg")

#2. crop image to fourth quadrant
h,w,d =I.shape
print ("The height of the image is ", h)
print ("The width of the image is ", w)
#size = np.shape(I)
#print ("The size of the image is ", size)
#C =I[208:416,149:298] #crops height then width
C =I[int(0.5*h):h,int(0.5*w):w] #crops height then width


#3. rotate cropped section
hn,wn,dn =C.shape
height_scale=h/hn
#print ("The height scale  is ", height_scale)
scale_check2=w/wn
#print ("The width scale  is ", scale_check2)


Qt=45 #desired angle to rotate
Qo=m.atan(hn/wn)#Gathers image's base hypotenuse angle in radians 
#print ("Qo ", Qo)
Qr=m.radians(Qt)
#print ("Qr ", Qr)
Q=Qo+Qr
#print ("Q ", Q)
hyp=m.sqrt(hn*hn + wn*wn)
#print ("hypotenuse ", hyp)
h1=(hyp)*(m.sin(Q))
#print ("h1 ", h1)
w1=(hyp)*(m.cos(Q))
#print ("w1 ", w1)

h1=round(h1)
w1=round(w1)
M =cv2.getRotationMatrix2D(center=(int(1.5*wn),int(0.5*hn)),angle=Qt, scale=1)
R =cv2.warpAffine(C, M = M,dsize=(w,h))
#M=cv2.getRotationMatrix2D(center=(75,104),angle=45, scale=1)
#R =cv2.warpAffine(C, M = M,dsize=(208,149))

#4. show images
cv2.imshow("Original",I)
#cv2.imshow("cropped",C)
cv2.imshow("cropped & rotated",R)
key =cv2.waitKey(0)

cv2.imwrite("Rotated_cropped_image.jpg",R)