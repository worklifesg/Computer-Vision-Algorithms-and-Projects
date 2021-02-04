'''
Program to enhance image using unsharping masking that can be done using either by
Gaussian, Median, Maximum and Minimum Filter

The radius setting is related to the blur intensity (as explained before) because it defines the size of the edges. 
The amount setting, on the other hand, controls the intensity of the edges (how much dark or light it will be).
'''

import cv2
from skimage import img_as_float
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.ndimage.filters import gaussian_filter, median_filter, maximum_filter, minimum_filter

###########################################################
###### Functions ##########################################
###########################################################

# function to read image and convert to gray scale

def read_image(image):
    image = cv2.imread(image)
    image = cv2.resize(image,(400,300))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    return gray

# function to select filter

def input_filter():
    print('Select the filter (1-Gaussian, 2-Median, 3-Max, 4-Min)')

    filter = int(input())
    print('Select the amount: ')
    amount = int(input())

    return filter,amount

image1 = '1_Chest_XRay.jpg'
image2 = '2_BrainTumor.jpg'
image3 = '3_HandSkeleton.jpg'

imagePaths = [image1,image2,image3]

filter,amount = input_filter()

if filter ==1:
    print("Value of radius: ")
    radius = int(input())

for i,imagePath in enumerate(imagePaths):

    gray = read_image(imagePath)
    gray = img_as_float(gray)

    if filter == 1:
        blur_image = gaussian_filter(gray,sigma=radius)
    elif filter == 2:
        blur_image = median_filter(gray,size=20)
    elif filter == 3:
        blur_image = maximum_filter(gray,size=20)
    else:
        blur_image = minimum_filter(gray,size=20)
        
    mask = gray - blur_image #to keep the edges
        
    sharp_image = gray + mask*amount
    sharp_image = np.clip(sharp_image,float(0),float(1))
    sharp_image = (sharp_image*255).astype(np.uint8)

    output_image = sharp_image

    cv2.imshow('Input Image',gray)
    cv2.imshow('Output Image',output_image)
    cv2.imwrite('Output_image_{}_{}.jpg'.format(filter,i),output_image)

    cv2.waitKey()
