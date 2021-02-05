#########################################################
############ UTILITY SCRIPT #############################
#########################################################

'''
Program to write utility function such as image pair generation,
computing euclidean distance, plot training history
'''

import tensorflow.keras.backend as K #to construct lambda layer to compute euclidean distance
import matplotlib.pyplot as plt 
import numpy as np 

#########################################################
############ IMAGE PAIR GENERATION ######################
#########################################################

def make_pairs(images,labels):

  #First we need to initialize image pairs (image,image) and labels (positive or negative) empty lists
  pairImages=[]
  pairLabels=[]

  #In our case images are digits visuals and classes are (0,9)

  #compute total number of unique class labels 
  numClasses = len(np.unique(labels)) #total number of classes
  idx = [np.where(labels == i)[0] for i in range(0,numClasses)] #list of indices for each class label

  #to loop over all images

  for idxA in range(len(images)):
    currentImage = images[idxA] #grab current image
    label = labels[idxA] #grab current image's label

    idxB = np.random.choice(idx[label]) #randomly pick an image corresponding to same class
    posImage = images[idxB] #label

    pairImages.append([currentImage,posImage]) #positive pair list updation
    pairLabels.append([1]) #indicating positive pair as 1

    negIdx = np.where(labels!= label)[0] #grab the indices where labels are not same as current label
    negImage = images[np.random.choice(negIdx)] #randomly picks an image where label is not same

    pairImages.append([currentImage,negImage]) #negative pair list update
    pairLabels.append([0]) #assigning '0' as negative pair

  return (np.array(pairImages),np.array(pairLabels))

#########################################################
############ EUCLIDEAN DISTANCE #########################
#########################################################

'''
vectors are outputs from FC layers of both sister networks
There is an in-built function in numpy to compute euclidean distance but here
we need to compute the result within the same architecture itself instead of
spearate layers. Thus Lambda layer is used to accomplish the task.
'''

def euclidean_distance(vectors):

    (featsA,featsB) = vectors #unpack vectors

    #computing the sum of squared distances
    sum_sq = K.sum(K.square(featsA-featsB),axis=1,keepdims=True)

    return K.sqrt(K.maximum(sum_sq,K.epsilon()))

#########################################################
############ PLOTTING FUNCTION  #########################
#########################################################

def plot_training(model_H,plotPath):
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(model_H.history["loss"], label="train_loss")
    plt.plot(model_H.history["val_loss"], label="val_loss")
    plt.plot(model_H.history["accuracy"], label="train_acc")
    plt.plot(model_H.history["val_accuracy"], label="val_acc")
    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="lower left")
    plt.savefig(plotPath)
