#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages
from keras.models import model_from_json
import tensorflow as tf
import numpy as np
from tensorflow import keras
import glob


# In[1]:


#preprocess the images and keep a list of the unprocessed images.
def process_images(data_path):
    files = glob.glob(data_path)
    data = []
    for f1 in files:
        img = keras.preprocessing.image.load_img(f1)
        #[m,n,k] = np.shape(img)
        #switch when new model is trained
        [m,n,k] = 64,64,3
        img_array = keras.preprocessing.image.load_img(f1, target_size=(m,n,k))
        img_array = keras.preprocessing.image.img_to_array(img_array)
        img_array /= 255
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        data.append(img_array)
        
    return data


# In[12]:


#use the CNN to predict if any of the images are likely to be cats and populate list if they are
def final_answer(data,loaded_model):
    is_cat = np.zeros(len(data))
    for i,img in enumerate(data):
        if loaded_model.predict(img)[0] > .5:
            is_cat[i] = 1
    return is_cat


# In[9]:


if __name__ == "__main__": 
    process_images()
    final_answer()

