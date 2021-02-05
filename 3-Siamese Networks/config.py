#########################################################
############ CONFIG FILE ################################
#########################################################

'''
Program for configuration of image size, batch size, epochs and output model and training history save
'''

import os

image_shape = (28,28,1) #MNIST digit image size with 28×28 pixels with a single grayscale channel

#batch size and epochs
batch_size = 64
epochs = 100

#output path folder

base_output = 'output'

#model path and training history path
model_path = os.path.sep.join([base_output,'siamese_model'])
plot_path = os.path.sep.join([base_output,'plot.png'])
