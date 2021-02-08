<h2 align='center'>Project Name : Image alignment and registration </h2>


**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Image Alignment and Registration is a technique where two **similar type** images are taken into account (viewing angles may be different) and wrap together to align themselves using homography matrix. The applications of image alignment and registration includes:

  - [ ] **Medical Images** - To better read different scan images such as MRI scans, SPECT scans and align them together to help specialist provide more accurate diagnosis
  - [ ] **Military** - Multiple images of target and aligning them using Automatic Target Recognition (ATR) to improve target recognition
  - [ ] **OCR** - Document images alignment in the context of feature based optical character recognition (OCR) to build automatic forms. 
  
In this work, we will study feature based algorithms for OCR - Document alignment by stacking together and also overlaying them.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Algorithms**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are different image alignment and registration algorithms used:

  * **Feature Based Algorithms** - Keypoint detectors (DoG, Harris,GFFT), local variant descriptors (SIFT,SURF,ORB) and keypoint matching (RANSAC) - **[[OCR}}**
  * **Similarity measure** - Cross-correlation, Sum of squared intensity differences, and Mutual Information - **[[Medical]]**
  * Deep Learning Algorithms **(Current State of the Art)** 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Images/Program**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The images used are **(2 scan images and one template)**

We will be using two programs
  * ![ocr_image_alignment.py]() - To define function for align images using openCV
  * ![ocr_document_alignment.py]() - to stack or overlay aligned and template images
