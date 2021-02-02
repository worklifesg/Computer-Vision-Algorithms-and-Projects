'''
Program to detect low contrast video and apply image processing techniques
'''

#import libraries
import cv2
from skimage.exposure import is_low_contrast
import imutils
import numpy as np 

video = cv2.VideoCapture('example_video.mp4')

#loop to iterate frames of videos
while True:
    grab,frame = video.read()

    #breaking condition
    if not grab:
        print('No frame to read')
        break

    frame = cv2.resize(frame,(300,400))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting the frame to gray scale
    blur = cv2.GaussianBlur(gray,(5,5),0)
    edge = cv2.Canny(blur,30,150)

    #intialize text on frame
    text = 'Low Contrast: NO'
    color = (0,255,0)

    if is_low_contrast(gray,fraction_threshold=0.35):
        text = 'Low Contrast: YES'
        color = (0,0,255)
    else:
        cnts = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)
		# draw the largest contour on the frame
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
    
    # draw the text on the output frame
    cv2.putText(frame, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8,color, 2)

    #stacking the output frame and edge map
    output = np.dstack([edge]*3)
    output = np.hstack([frame,output])

    cv2.imshow('Output',output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    


