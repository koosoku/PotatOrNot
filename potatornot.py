import numpy as np
import cv2

potato_cascade = cv2.CascadeClassifier('potato_cascade.xml')

img = cv2.imread('tests\potato1.jpg');
img = cv2.resize(img, (450 , 300))
gray_potato = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

potatoes = potato_cascade.detectMultiScale(gray_potato, 10, 10)

# add this
for (x,y,w,h) in potatoes:
    cv2.rectangle(img,(x,y),(x+w,y+h))

cv2.imshow('img',img)
cv2.waitKey(0)