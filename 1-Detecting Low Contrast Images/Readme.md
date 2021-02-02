<h2 align='center'>Project Name : Detecting low contrast images with OpenCV, scikit-image, and Python </h2>

**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is easier to write image processing codes with ***good lighting*** conditions and code techniques such as blurring, edge-detections, thresholding etc. But in real-world data, sometimes having a ***controlled image*** is not possible, so we need to detect low quality image, specifically low contrast images.

**Problems created by low contrast images** - Little difference between light and dark regions (boundary detection becomes difficult)

**Libraries used** - OpenCV, scikit-image

In this project, we will cover 2 aspects of low contrast images:
  ```diff
  + Detect Low Contrast in Static Images
  + Detect Low Contrast Frames in Real-Time Video Streams
  ```

**Detect Low Contrast in Static Images**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this project, we take an image of Lung CT scan
