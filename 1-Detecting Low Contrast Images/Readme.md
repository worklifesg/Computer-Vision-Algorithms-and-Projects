<h2 align='center'>Project Name : Detecting low contrast images with OpenCV, scikit-image, and Python </h2>

**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is easier to write image processing codes with ***good lighting*** conditions and code techniques such as blurring, edge-detections, thresholding etc. But in real-world data, sometimes having a ***controlled image*** is not possible, so we need to detect low quality image, specifically low contrast images.

**Problems created by low contrast images** - Little difference between light and dark regions (boundary detection becomes difficult)

**Libraries used** - OpenCV, scikit-image

In this project, we will cover 2 aspects of low contrast images:
  ```diff
  + Detect Low Contrast in Static Images (on Lung CT Scan)
  + Detect Low Contrast Frames in Real-Time Video Streams (General Application)
  ```

**Detect Low Contrast in Static Images**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- [x] In this project, we take an image of Lung CT scan (high contrast image) and generate a low contrast image with 35% threshold value ![[Code]](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/2-generate-low-contrast-image.py)

<p align="center">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/images/test_image.jpeg">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/images/test_image_low_contrast.jpg">
</p> 

<h4 align="center">
  High Contrast Image -------------------> Low Contrast Image
</h4> 

- [x] Use ![[Detect Low Contrast Image]](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/1-detect-low-contrast.py) code where:

  - [x] Read both images (low & high contrast images)
  - [x] Define Watershed Algorithm
  - [x] Loop to iterate each image for image processing techniques

- [x] Results:

<p align="center">
  <img width="450" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/images/Image_t2.JPG">
  <img width="450" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/1-Detecting%20Low%20Contrast%20Images/images/Image_t1.JPG">
</p> 
