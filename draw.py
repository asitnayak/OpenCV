import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
'''
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)
'''

# 2. Draw a Rectangle
'''
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)  # thickness=-1 , for filled
cv.imshow('Rectangle', blank)
'''

# 3. Draw a circle
'''
cv.circle(blank, (250,250), 40, (0,0,250), thickness=-1)
cv.imshow('Circle', blank)
'''

# 4. Draw a line
'''
cv.line(blank, (0,0), (250,250), (250,250,250), thickness=3)
cv.imshow('Line', blank)
'''

# 5. Write text
cv.putText(blank, 'WassUp', (225,225), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

'''
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)
'''

cv.waitKey(0)