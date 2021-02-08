from ocr_image_alignment import align_images
import numpy as np
import imutils
import cv2

#Read the image and the template
image= cv2.imread('scan_01.jpg')
template = cv2.imread('form_w4.png')

aligned = align_images(image, template, debug=True)

#resize for better visualization

aligned = imutils.resize(aligned,width=700)
template = imutils.resize(template,width=700)

#visualization of documents side by side
stacked = np.hstack([aligned,template]) #first apporach
overlay = template.copy()
output = aligned.copy()
cv2.addWeighted(overlay,0.5,output,0.5,0,output)

cv2.imshow("Image Alignment Stacked", stacked)
cv2.imshow("Image Alignment Overlay", output)
cv2.imwrite("stacked2.jpg",stacked)
cv2.imwrite("overlay2.jpg",output)
cv2.waitKey(0)
