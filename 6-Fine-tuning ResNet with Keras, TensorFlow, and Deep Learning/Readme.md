<h2 align='center'>Project Name : Fine-tuning ResNet with Keras, TensorFlow, and Deep Learning </h2>


**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ResNet stands for Residual Network Deep Learning Architecture that was first introduced by ![He et al. in 2015](https://arxiv.org/abs/1512.03385) and modifying the residual components of the architecture in the ![Identify Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027). It is one of an important architecture after AlexNet (2012), VGGNet (2014),and GoogLeNet (2014)

<p align="center">
  <img width="500" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning/images/ResNet_He_et_al_2016.png">
</p> 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Concept of ResNet**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Identify mappings means taking the original input to the module and adding it to the output of a series of operations. For instance, we take an input and apply convolution networks (general) and the output is added with the original input. This addition of input adding directly to the output is ***linear shortcut*** (connection between input and output). SUch type of residual frameworks allows us to train networks **more substantially deeper**. As input is included in every residual module, it turns out that the network can **learn faster** and with **larger learning rates.**

Another variation of **Residual Networks** is **Bottleneck** that serves as dimensionality reduction (reducing total number of parameters in the network while retaining the accuracy as well)

Another concept is **Pre-activation** which means to rearrange the order of operations (convolution, batch normalization, activation) which can lead to **better and higher accuracy models that are easier to train**

<p align="center">
  <img width="200" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning/images/fine_tune_resnet_residual_orig.png">
  <img width="200" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning/images/fine_tune_resnet_residual_bottleneck.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/6-Fine-tuning%20ResNet%20with%20Keras%2C%20TensorFlow%2C%20and%20Deep%20Learning/images/fine_tune_resnet_residual_preactivation.png">
</p> 


------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Fine-Tuning of ResNet**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fine-tuning of ResNet is very useful in using the pre-trained weights only (no output fully connected layer) for different projects and applications. The fine-tuning process is as follows:

  * Using pre-trained ResNet (from Keras)
  * Removing fully connected (FC) layer head from network
  * Add a customized new layer on top of the network body
  * Optionally freezing the weigths for the layers
  * Training the model using **pre-trained weigths + new head layer**


------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Dataset used in this project**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here in this project, we will use dataset **(camouflage vs. normal clothing dataset)** compiled by ![Julia Riede](https://github.com/jriede/ml-data/tree/master/camouflage-clothing) and ![Nitin Rai](https://twitter.com/imneonizer/status/1225749289491554305) and implemented by ![Adrain Rosebrock](https://www.pyimagesearch.com/2020/04/27/fine-tuning-resnet-with-keras-tensorflow-and-deep-learning/)
