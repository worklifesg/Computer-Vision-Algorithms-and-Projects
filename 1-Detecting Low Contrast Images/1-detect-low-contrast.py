'''
Program to detect low contrast images of chest X-rays and apply images processing techniques
'''

#import libraries
import cv2
from skimage.exposure import is_low_contrast
import imutils
import numpy as np 

'''
Here we set thresholding as 35% i.e. range of brightness that occupy full range of data type
it is considered as low-contrast
'''
#path of input images

image1='test_image.jpeg'
image2='test_image_low_contrast.jpg'

imagePaths = [image1,image2]
kernel=np.ones((7,7),np.uint8)

##################################################################################
########################### Watershed Algrotihm ##################################
##################################################################################

def watershed(sure_fg,gray,sure_bg,image):
    #######Waterhsed algorithm

    contours, hierarchy = cv2.findContours(sure_fg,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

     #numpy array for amrkers 

    marker = np.zeros((gray.shape[0],gray.shape[1]),dtype=np.int32)
    marker = np.int32(sure_fg)+np.int32(sure_bg)

    #marker labeling

    for i in range(len(contours)):
        cv2.drawContours(marker,contours,i,i+2,-1)
        
    marker = marker + 1 #to make sure background is not black 0
    marker[unknown==255] = 0 #unknown regions as 0 

    copy_img = image.copy()
    cv2.watershed(copy_img,marker)

    copy_img[marker == -1] = [255,0,255]

    return copy_img

##################################################################################
###### Loop to perform contour detection using image processing techniques ########
##################################################################################

for (i,imagePath) in enumerate(imagePaths):
    print('processing image {}/{}'.format(i+1,len(imagePaths)))

    image = cv2.imread(imagePath) #read
    image= cv2.resize(image,(400,300))

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #to gray scale

    #### blur
    img_median = cv2.medianBlur(gray,5)
    #edge detection using sobelX, sobelY
    img_sobelx = cv2.Sobel(img_median,cv2.CV_8U,dx=1,dy=0,ksize=3)
    img_sobely = cv2.Sobel(img_median,cv2.CV_8U,dx=0,dy=1,ksize=3)

    img_sobel = img_sobelx+img_sobely+gray

    ret, th1 = cv2.threshold(img_sobel,55,255,cv2.THRESH_BINARY)

    #having foreground and background image
    kernel = np.ones((3,3),np.uint8)
    # To remove any small white noises in the image using morphological opening
    opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN,kernel,iterations=2)

    #background
    # Black region shows sure background area
    # Dilation increases object boundary to background.
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    #white region shows sure foreground region
    dist = cv2.distanceTransform(opening,distanceType=cv2.DIST_L2, maskSize=5)

    ret,sure_fg = cv2.threshold(dist, 0.2*dist.max(),255,0) #threshold value needs to change if tumor is not segmented 

    # Identifying regions where we don't know whether foreground and background
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    #####################################################

    text = 'Low Contrast: NO'
    color = (0,255,0)

    #to check if image is low contrast or not
    if is_low_contrast(gray,fraction_threshold=0.25):
        text = 'Low Contrast: YES'
        color = (0,0,255)
        copy_img = watershed(sure_fg,gray,sure_bg,image)
    
    else: #else we can continue to find contours of the edge map
        copy_img = watershed(sure_fg,gray,sure_bg,image)

    #todraw text on image
    cv2.putText(image,text,(5,25),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,thickness=2)

    #output
    cv2.imshow('Image',image)
    cv2.imshow('Edge',copy_img)
    cv2.imwrite('Image_{0}.jpg'.format(i),copy_img)
    cv2.waitKey(0)
