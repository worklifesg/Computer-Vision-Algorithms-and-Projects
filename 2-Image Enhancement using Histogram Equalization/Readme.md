<h2 align='center'>Project Name : Image Enhancement (Histogram Equalization, CLAHE, HEF, UM) </h2>

**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The objective of this project is to improve the visualization (image enhancement) of the medical images (CT,MRI scans) using image-processing techniques.

**Histogram Equalization** is a simple image processing technique that can improve an image's overall contrast. The idea of histogram equalization is to spread the gray scale image pixels to buckets that don't have as many pixels binned to them. Strictly speaking in mathematics terms, it means to apply linear trend to cummulative distribution function (CDF). However, using this technique, the image's contrast is significantly improved at the expense of boosting the noise present in the image.

**Unsharp Masking (UM)** technique implements a linear filter (i.e. steps of different convolutions) that can amplify high-frequencies of an image. The stpes include **applying Gaussian Blur**, and **Edges** that is obtained by subtracting blurred image from original image. Finally the enhanced image can be obtained using using certain weightage applied to the unsharped mask obtained by subtraction before.

**High Frequency Emphasis (HEF) Filtering** uses Gaussian HF filter that is used to emphasis and highlight the edges. In general, edges describes the high frequency points as there are high intensity changes along them. The enhanced image is obtained through following certain steps: **Applying GHF filter to image, FFT Analysis, compute filter function on it, Inverse FFT to get filtered image and apply histogram equalization to achieve sharpened image.

**Contrast Limited Adaptive Histogram Equalization (CLAHE)** is an adaptive histogram equalization technique to improve the contrast of an image. We comoute histogram for the region around each pixel in an image to give **local contrast** and **edge enhancement**. CLAHE prevents overamplification of the noise unlike simple histogram equalization. 

**Steps for CLAHE**

  - [ ] Gray Scale + Normalize
  - [ ] Image Padding
  - [ ] Compute clipped histogram for each pixel
  - [ ] Calculate probability of each pixel
  - [ ] Compute CDF - all pixels have transformation value
  - [ ] Apply transformation to the center of region

  * Clip limit should not be high as noise might become dominant and leads to simple histogram equalization
  * Computationally very time consuming and needs more power

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Credits

![UM, HEF, CLAHE - X-Ray Images Enhancement](https://github.com/asalmada/x-ray-images-enhancement)
