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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Part B : Training Siamese Networks with keras, TensorFlow, and Deep Learning**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next step is to build and train **siamese networks (subnetworks)** that has two inputs (either negative or positive pairs). The idea here is to find the similarity between two images that is computed using euclidean distance and using sigmoid function.

The training process include different python scripts that are used to define essential parameter definitions that will be use while training siamese network. These include:

  - [ ] **![config.py](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/config.py)** - . Paths, I/P image spatial dimensions, batch size, number of epochs
  - [ ] **![siamese_network.py](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/siamese-network.py)** - CNN model using Keras, and TensorFlow
  - [ ] **![utils.py](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/utils.py)** - functions related to building image pairs, computing euclidean distance, and plotting training measure history results
  
  - [ ] **![siamese-networks-training.ipynb](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/2_siamese_networks_training.ipynb)** - main training script that constitutes above 3 python scripts
    * Load and read MNIST digit dataset (config.py)
    * Build positive and negative pairs (utils.py)
    * Build siamese network architecture (siamese_network.py)
    * Train the siamese network
    * Training History (Loss and Accuracy) - (utils.py)

To run 100 epochs, either we need a GPU or TPU with high RAM. The main script is run on Google Colab (However due to certain reasons, the model was not training properly under GPU-HighRAM but worked well with TPU-HighRAM (a bit slower than GPU for images)).

***Result***

The model is saved as and the training history plot is given as:

<p align="center">
  <img width="500" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/plot.png">
 </p> 

The model obtained around 88% of accuracy on testing dataset.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Part C : Comparing images using Siamese Networks**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once the Siamese network is trained, we can predict results for other input images (i.e. compare the imaes and evaluate the similarity between them.

We have chosen certain images for test that will be compared and evaluaed using siamese network. The images are:

<p align="center">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_01.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_02.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_03.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_04.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_05.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_06.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_07.png">
 </p>
<p align="center">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_08.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_09.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_10.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_11.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_12.png">
  <img width="100" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/test_images/image_13.png">
 </p> 

The output of the model is saved in ![[output]](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/output.zip) and used to load the model trained in Part B. 

***Results:***


<p align="center">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction2.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction3.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction4.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction5.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction6.png">
 </p>
<p align="center">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction7.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction8.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction9.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction10.png">
  <img width="250" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/3-Siamese%20Networks/images/prediction11.png">
 </p> 
