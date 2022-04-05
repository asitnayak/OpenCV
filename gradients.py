import cv2 as cv
import numpy as np

img = cv.imread("Photos/dog_1.jpg")
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny
canny = cv.Canny(gray, 100, 175)
cv.imshow('Canny', canny)

canny1 = cv.Canny(gray, 150, 175)
cv.imshow('Canny1', canny1)

canny2 = cv.Canny(gray, 200, 175)
cv.imshow('Canny2', canny2)


cv.waitKey(0)