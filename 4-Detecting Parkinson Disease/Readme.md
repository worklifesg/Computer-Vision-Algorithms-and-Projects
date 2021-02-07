<h2 align='center'>Project Name : Detecting Parkinson’s Disease with OpenCV, Computer Vision, and the Spiral/Wave Test </h2>


**Introduction**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Parkinson's Disease is a nervous system disorder that effects movement. There is no cure for Parkinson but with proper medication and environment can improve symptoms and quality of life. Such type of disease is progressive in nature and has 5 different stages.


  Stages of Parkinson's Disease|
  |----------|
  |**Stage I:** Mild symptoms - bit of tremors and movement issues on only side of the body. |
  |**Stage II:** Symptoms grow more with small tremors and mmovements on both sides of the body. |
  |**Stage III:** Loss of balance and movements with falls more frequent and common. Can still live independently. |
  |**Stage IV:** Severe and constraining symptoms. Unable to live alone and needs assistance for daily activities |
  |**Stage V:** Likely possible to walk and stand. Wheelchair bound and may even experience hallucinations. |

Generally patients are told to **draw spirals and waves** to detect Parkinson that can be evaluated from **speed of drawing and pen pressure**.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Dataset**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The dataset used in this study is curated by Adriano de Oliveira Andrade and Joao Paulo Folado from the ![NIATS of Federal University of Uberlândia](http://www.niats.feelt.ufu.br/en/node/81) and looks somewhat like this ![[PyImageSearch Fig.3]](https://www.pyimagesearch.com/2019/04/29/detecting-parkinsons-disease-with-opencv-computer-vision-and-the-spiral-wave-test/):

<p align="center">
  <img width="500" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/detect_parkinsons_dataset.jpg">
</p> 

The dataset consists of:
  - [ ] Spiral - 102 images (72 training and 30 testing)
  - [ ] Wave - 102 images (72 training and 30 testing)
  
However the dataset is not much for model to have proper training, though some researchers have used deep learning algorithms and architectures ![[Kaggle notebooks]](https://www.kaggle.com/kmader/parkinsons-drawings) but one of the point made by ![[Adrian Rosebrock]](https://www.pyimagesearch.com/2019/04/29/detecting-parkinsons-disease-with-opencv-computer-vision-and-the-spiral-wave-test/) is that using architecture such as ResNet, we are doing transfer learning via feature extraction and not training the network. The author himself used RandomForestClassifier to achieve **83.33% (Spiral) and 71.33% (Wave)**

Moreover, we can try to augment data but in this context also, it can be quite problematic as we might train a network making a healthy patient drawing look like Parkinson's patient or vice-versa.

**However we will try to avoid artificial neural networks and try to implement RandomForest Classifier, AdaBoost Classifier and XGBoost Classifier and compare training and testing accuracy and low loss. The implementation of the program is done on Google Colab**

  * The program for Spiral Training and Testing can be found ![here](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/parkinson_spiral_training.ipynb)
  * The program for Wave Training and Testing can be found ![here](https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/parkinson_wave_training.ipynb)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Results**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Dataset | RandomForest Classifier | AdaBoost Classifier  | XGBRegressor | 
| ------------- | ------------- | ------------- | ------------- |
| Spiral | 86.67 % | 70 % | 83.33% |
| Wave | 73.33 % | 63.33 % | 70% |

**Spiral Dataset Prediction (RandomForest Classifier | AdaBoost Classifier  | XGBRegressor)**

<p align="center">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/spiral_RF.png">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/spiral_Ada.png">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/spiral_XGB.png">
</p> 

**Wave Dataset Prediction (RandomForest Classifier | AdaBoost Classifier  | XGBRegressor)**

<p align="center">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/wave_RF.png">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/wave_Ada.png">
  <img width="300" alt="java 8 and prio java 8  array review example" img align="center" src ="https://github.com/worklifesg/Computer-Vision-Algorithms-and-Projects/blob/main/4-Detecting%20Parkinson%20Disease/images/wave_XGB.png">
</p> 


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Fine Tuning of XGBoost**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fine tuning of XGBoost classifier can be performed using Dmatrix and running this algorithm more efficiently. The fine tuning can be found for both dataset in their respective programs in the end. **The testing ROC-AUC score obtained is 94.67% and 80% for spiral and wave dataset respectively.**
