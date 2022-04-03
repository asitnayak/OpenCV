import cv2 as cv

'''
img = cv.imread("Photos/cat.jpg")
cv.imshow('Cat', img)
'''

def rescaleFrame(frame, scale=0.75):
    # Images, Videos, Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

'''
rescaled_img = rescaleFrame(img, scale=0.2)
cv.imshow('Rescaled Img', rescaled_img)
cv.waitKey(0)
'''

# Reading Videos
capture = cv.VideoCapture('Videos/vidd.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Rescaled Video', frame_resized)

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()