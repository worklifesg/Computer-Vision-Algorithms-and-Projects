<h2 align='center'>Project Name : Siamese Networks (Image Pairs, Training using Keras, TF, DL and Comparing Images) </h2>


**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Siamese networks are inspired from the term **"siamese twins"** which means **"conjoined twins"** that are connected to each other (difficult to separate)

In neural networks, **"siamese networks"** are special class that contains two or more identical subnetworks (same architecture, parameters, and weights). Any changes in one network will update other network parameters as well. This feature of siamese networks can be widely used in applications such as **face recognition, signature verification** as well as can be extended to **medical imaging** (evaluating the severity of the disease ![Reading paper](https://www.nature.com/articles/s41746-020-0255-1)).

Example |
|----------|
| **Detecting signature forgeries** - In general, we classify model to correctly classify signature based on their training using image classification networks. Here in **siamese networks**, we will use two images as an input from training dataset and ask the neural network if the signature were from the same person or not? |

![Reference](https://arxiv.org/abs/1707.02131) 
<p align="center">
  <img width="500" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/siamese_image_pairs_signet.png">
 </p> 

Steps in Siamese Networks (above figure) |
|----------|
|1. Input two signatures to SigNet model (architecture used). Goal is to determine if these signatures are similar or not.|
|2. Middle layer comprise of 2 similar (mirror) dependent architectures |
|3. The final layers in the architecture are **embedding layers** that compute **Euclidean distance** between O/P and adjust the weights to obtain correct decision |
|4. In the last, we have a **loss function** that combines outputs from subnetworks and checks if the siamese network made correct decision or not. |
|5. Popular Loss functions - **Binary Cross-Entropy, Triplet Loss, Contrastive Loss**|

This project is divided into three segments:

  - [ ] Building Image Pairs for Siamese Networks
  - [ ] Training Siamese Networks with keras, TensorFlow, and Deep Learning
  - [ ] Comparing images using Siamese Networks
  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Part A: Building Image Pairs for Siamese Networks**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To train a siamese network, we need **image pairs** that can be **positive pairs** and **negative pairs**

  * **Positive pairs** - Two images belonging to **same** class (images of same person, same signatures etc.)
  * **Negative pairs** - Two images belonging to **different** class (images of different people, different signatures etc.)

In this ![[program]](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/1_image_pairs_siamese_networks.ipynb), we used ![MNIST digit dataset](http://yann.lecun.com/exdb/mnist/) where each similar looking digits are classified as positive pairs with respect to the same class else others are classified as negative pairs. ```build_montages``` is used to build a montage of 49 images (7 x 7) with proper labeling as 'pos' and 'neg' for positive and negative pairs respectively. 

The logic behind making pairs is to put together images with same classes (i.e. (0-9) in this case) and also images with different classes (i.e. 0 with 1 or 1 with 2 etc.). The images are chosen randomly and then pairing process is further proceeded.

***Result***

<p align="center">
  <img width="500" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/Image_Pairs.jpg">
 </p> 



