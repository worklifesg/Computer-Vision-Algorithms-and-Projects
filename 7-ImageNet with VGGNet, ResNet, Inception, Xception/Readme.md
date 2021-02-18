<h2 align='center'>Project Name : ImageNet with VGGNet, ResNet, Inception, Xception </h2>


**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Convolution Neural Networks are used to classify images and are pre-trained on ![ImageNet](http://www.image-net.org/) that can recognize more than 1000 different object categories. However, the pre-trained ImageNet models are available on Keras with pre-trained networks such as VGG16, VGG19, ResNet50, InceptionV3, ande Xception. Their base source codes can be found in ![Keras Github](https://github.com/keras-team/keras/tree/master/keras/applications).

In this project, we will study fundamental difference between these networks and using these pre-trained networks, we can classify our own custom input images


<h2 align='center'> Theory Concepts </h2>


**ImageNet**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ImageNet is a project designed to manual label and categorize images into around 22,000 separate object categories. There are around 1.4 million images (original and url links) available that has 50,000 images for validation and 100,000 images for testing. The challenge posted by ImageNet was to correctly classify an input image into 1000 separate object categories. The pre-trained networks were included in Keras  library that has benn benchmark for computer vision classification algorithms.


**VGG16, VGG19**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

VGG architecture was introduced in 2014 for very deep convolution networks. VGG stands for the team that participated in ImageNet challenge. VGG network is very simple with 3 x 3 convolution layers stacked on top of each other. The volume is reduced by using max pooling layers. In the end there are 2 fully-connected (FC) layers each with 4096 nodes followed by softmax classifier. 

There are different weight layers in the networks such as starting with **11-weight layers** (basically for pre-training) and going up to **16-weight layers** and **19-weight layers**. **16 and 19** are considered very deep layers and VGG16 and VGG19 faced challenges to converge on the deeper networks. So the training with smaller weight layers made convergence possible that were used as initialization for the larger and deeper networks.

There are two drawbacks for VGG:

  * Slow to train
  * Network Architecture weights themselves quite large
  
**ResNet**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As explained in ![Project 6](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/tree/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning), ResNet means to indentify mappings. Identify mappings means taking the original input to the module and adding it to the output of a series of operations. For instance, we take an input and apply convolution networks (general) and the output is added with the original input. The theory behind ResNet architecture and its fine tuning can be found in ![Project 6](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/tree/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning).

ResNet offers more deeper layers with weights (depths) from 50-200 with very low computation storage need. **For instance ResNet50 reduces the model size to 102 MB as compared to 533 MB of VGG16 and 574 MB of VGG19.

  
**Inception**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Inception was first introduced in 2014 with this ![publication](https://arxiv.org/abs/1409.4842). This architecture deals with **multi-level feature extractor** by computing 1 x 1, 3 x 3, 5 x 5 convolutions within the same module of the network. The output of these filters is stacked along channel dimension before proceeding to the next layer in the network. Put simply, it allows for us to use multiple types of filter size, instead of being restricted to a single filter size, in a single image block, which we then concatenate and pass onto the next layer.

The original idea rose as GoogLeNet architecture, where later versions of Inception are known as ***Inception VN*** such **Inception V3** that will discussed and implemented here in this project. The model size is less than both ResNet50 and VGG networks.

**Xception**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Xception was proposed by the creator of Keras library in 2015, where it is just an extension of Inception architecture which replaces Inception modules with depthwise separable convolutions. The model size is less than all the networks stated above.



