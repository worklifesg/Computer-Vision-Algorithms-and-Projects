#########################################################
############ NETWORK ARCHITECTURE #######################
#########################################################

'''
Program to write siamese network architecture (CNN model)
using tensorflow and keras
'''

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D,Dense,Dropout,GlobalAveragePooling2D,MaxPooling2D

def build_siamese_network(inputShape, embeddingDim=48):
    #embeddingDim - output dimension of FC layer 

    inputs = Input(inputShape) #inputs for the feature extractor

    #First Layer Set
    x = Conv2D(64,(2,2), padding='same',activation='relu')(inputs)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.3)(x)

    #Second Layer Set
    x = Conv2D(64,(2,2), padding='same',activation='relu')(x)
    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.3)(x)

    #final outputs
    pool_output = GlobalAveragePooling2D()(x)
    outputs = Dense(embeddingDim)(pool_output)

    #build model
    model = Model(inputs,outputs)

    return model
    


