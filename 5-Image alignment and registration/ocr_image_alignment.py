######################################
##### Image Alignment ################
######################################

#Import libraries
import numpy as np 
import imutils
import cv2

def align_images(image,template,maxFeatures=500,keepPercent=0.9,debug=False):
    #convert image and template to gray scale
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_temp = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

    #using orb detector to detect keypoints and extract local invariant features
    orb = cv2.ORB_create(maxFeatures)
    (kpsA,descsA) = orb.detectAndCompute(gray_image,None)
    (kpsB,descsB) = orb.detectAndCompute(gray_temp,None)

    #match features
    '''
    Hamming method is used to compute distance between binary features to find best matches
    '''
    method = cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
    matcher = cv2.DescriptorMatcher_create(method)
    matches = matcher.match(descsA,descsB,None)

    '''
    Sorting, Filtering, and Displaying
    '''
    matches = sorted(matches, key=lambda x:x.distance)

    #to keep only top matches
    keep = int(len(matches)*keepPercent)
    matches=matches[:keep]

    #to visualize keypoints
    if debug:
        matchedVis = cv2.drawMatches(image,kpsA,template,kpsB,matches,None)
        matchedVis = imutils.resize(matchedVis, width=1000)

        cv2.imshow("Matched Keypoints", matchedVis)
        cv2.waitKey(0)
    
    # allocate memory for the keypoints (x,y-coordinates) from the
	# top matches -- we'll use these coordinates to compute our
	# homography matrix

    ptsA = np.zeros((len(matches),2),dtype='float')
    ptsB = np.zeros((len(matches),2),dtype='float')

	# loop over the top matches
    for (i, m) in enumerate(matches):
        # indicate that the two keypoints in the respective images
        # # map to each other
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt

	# compute the homography matrix between the two sets of matched
	# points
    (H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)

	# use the homography matrix to align the images
    (h, w) = template.shape[:2]
    aligned = cv2.warpPerspective(image, H, (w, h)) #to align the iamges

	# return the aligned image
    return aligned

#image= cv2.imread('scan_01.jpg')
#template = cv2.imread('form_w4.png')

#align_images(image, template, debug=True)




