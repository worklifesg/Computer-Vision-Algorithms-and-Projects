'''
Program to apply histogram equalization and CLAHE algorithm using OpenCV
Credits: PyImageSearch
'''

import cv2

image1 = '1_Chest_XRay.jpg'
image2 = '2_BrainTumor.jpg'
image3 = '3_HandSkeleton.jpg'

imagePaths = [image1,image2,image3]

### text on images
text1 = 'HISTOGRAM EQUALIZATION'
text2 = 'CLAHE'
color = (0,0,255)


#function for histogram equalization
def hist_eq(gray):
    hist_eq_out = cv2.equalizeHist(gray)
    return hist_eq_out

def hist_clahe(gray):
    clahe= cv2.createCLAHE(clipLimit=40,tileGridSize=(8,8))
    hist_clahe_out = clahe.apply(gray)
    return hist_clahe_out


for (i,imagePath) in enumerate(imagePaths):
    print('processing image {}/{}'.format(i+1,len(imagePaths)))

    image = cv2.imread(imagePath) #read the image
    image = cv2.resize(image,(400,300))

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    hist_eq1 = hist_eq(gray)
    clahe_eq = hist_clahe(gray)

    cv2.putText(hist_eq1,text1,(5,25),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,thickness=2)
    cv2.putText(clahe_eq,text2,(5,25),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,thickness=2)

    cv2.imshow('Input',gray)
    cv2.imshow('Enhanced_image_histogram',hist_eq1)
    cv2.imshow('Enhanced_image_CLAHE',clahe_eq)
    cv2.waitKey(0)


