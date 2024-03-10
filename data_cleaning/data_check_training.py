# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:02:55 2024

@author: Ivan Balkanski ID: 40151720
"""

import os
from skimage import io
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import ImageGrid
import random
import skimage as ski


# uncomit the type of data you want to analyze
# commit the other one

#data = "data/test/"
data = "data/train/"

#data_array = ["angry/test_angry_","surprise/test_suprise_","neutral/test_neutral_","sad/test_sad_","fear/test_fear_"]
data_array = ["angry/training_angry_","surprise/training_suprise_","neutral/training_neutral_","sad/train_sad_","fear/train_fear_"]


#controls the range of the random numbers generated
# for best results set it to 730 for the test data and max up to 3000 for the train data
range_upper_limit = 3000


# matrix with 5 rows each 25 colums
img_array = q = [ [ None for l in range(25) ] for m in range(5) ]

#index for array row
arr_index = 0
for j in data_array:
    num_location = 0
    while num_location < 25:
        img_name =  data + j + str(random.randint(1, range_upper_limit)) +".jpg"
        #checks if image exists 
        if os.path.exists(img_name):
           # print(img_name)
           # puts image in array[row][col]
            img_array[arr_index][num_location] = io.imread(img_name,as_gray=True)
            #updates colum number
            num_location = num_location+1
    #updates row number
    arr_index = arr_index+1


# index for current figure plot
fig_num = 1
#index for current image arrays used
arr_grid_num = 0
#loop through the matrix for each array of images
#creating a  5x5 grid followed by each images histogram
for i in data_array:
    #creates a new figure
    fig = plt.figure(fig_num,figsize=(4., 4.))
    # creates a grid that is 5x5
    grid = ImageGrid(fig, 111,  
                 nrows_ncols=(5, 5),  # creates 5x5 grid of axes
                 axes_pad=0.1,  # pad between axes in inch.
                 label_mode="1", # adds label only at end
                 )
    # get label name from current class
    label_name = i.split("/")[0]
    for ax, im in zip(grid, img_array[arr_grid_num]):
        # Iterating over the grid returns the Axes.
        ax.imshow(im,cmap="gray")
        ax.set_xlabel(label_name)
        
    for current_img in img_array[arr_grid_num]:
        #converts image to point format
        float_img = ski.util.img_as_float(current_img)
        fig_num = fig_num+1
        #displays image
        histogram, bin_edges = np.histogram(float_img, bins=256, range=(0, 1))
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.ylabel("pixel count")
        plt.xlim([0.0, 1.0])  # <- named arguments do not work here
        plt.plot(bin_edges[0:-1], histogram)  # <- or here
        
        
    fig_num = fig_num+1
    #increment for next array list
    arr_grid_num = arr_grid_num+1

plt.show()

