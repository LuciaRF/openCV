import cv2 as cv # type: ignore

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.2):
    #Images, Videos live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resize_image = rescaleFrame(img)
cv.imshow('Image',resize_image)

def changeRes(width,height):
    #Live video
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resize = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resize)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
capture.destroyAllWindows()
