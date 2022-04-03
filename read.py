import cv2 as cv

# Reading Image
'''
img = cv.imread("Photos/cat.jpg")

cv.imshow('Cat', img)

cv.waitKey(0)

'''

# Reading Videos
capture = cv.VideoCapture('Videos/vidd.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

