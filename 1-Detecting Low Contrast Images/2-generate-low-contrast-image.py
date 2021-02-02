'''
Program to generate low contrast image using openCV
'''

import cv2
import numpy as np 

source = 'test_image.jpeg'

source_image = cv2.imread(source)

output_image = np.zeros(source_image.shape,source_image.dtype)

alpha = 0.35 #controlling contrast of image
beta = 1 #controlling brightness of image


'''
We can use cv2.convertScaleAbs(image,alpha=alpha,beta=beta) directly but 
we will use for loop to show how to access pixels
'''

for y in range(source_image.shape[0]):
    for x in range(source_image.shape[1]):
        for c in range(source_image.shape[2]):
            output_image[y,x,c] = np.clip(alpha*source_image[y,x,c]+beta,0,255)

cv2.imshow('Original Image', source_image)
cv2.imshow('New Image', output_image)

cv2.imwrite('test_image_low_contrast.jpg',output_image)
# Wait until user press some key
cv2.waitKey()
