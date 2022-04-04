import cv2 as cv

img = cv.imread("Photos/dog_1.jpg")
cv.imshow('Dog', img)

# Averaging (Does the most blur)
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur (Blurs by assigning some weights to the kernel pixels)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (Used in noise reduction. Ideal size is 3)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral (The most effective. It applies bluring, but retains the edges.)
bilateral = cv.bilateralFilter(img, 10, 30, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)