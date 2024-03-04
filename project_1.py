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



# uncomit the type of data you want to analyze
# commit the other one

#data = "data/test/"
data = "data/train/"

#data_array = ["angry/test_angry_","surprise/test_suprise_","neutral/test_neutral_"]
data_array = ["angry/training_angry_","surprise/training_suprise_","neutral/training_neutral_"]


#controls the range of the random numbers generated
# for best results set it to 730 for the test data and max up to 3000 for the train data
range_upper_limit = 3000


# matrix with 3 rows and 25 colums
img_array = q = [ [ None for l in range(25) ] for m in range(3) ]


arr_index = 0
for j in data_array:
    num_location = 0
    while num_location < 25:
        img_name =  data + j + str(random.randint(1, range_upper_limit)) +".jpg"
        #checks if image exists 
        if os.path.exists(img_name):
           # print(img_name)
            img_array[arr_index][num_location] = io.imread(img_name,as_gray=True)
            num_location = num_location+1
    arr_index = arr_index+1



fig_num = 1
arr_grid_num = 0
#loop through the matrix for each array of images
#creating a  5x5 grid followed by each images histogram
for i in data_array:
    fig = plt.figure(fig_num,figsize=(4., 4.))
    grid = ImageGrid(fig, 111,  
                 nrows_ncols=(5, 5),  # creates 5x5 grid of axes
                 axes_pad=0.1,  # pad between axes in inch.
                 )
    for ax, im in zip(grid, img_array[arr_grid_num]):
        # Iterating over the grid returns the Axes.
        ax.imshow(im,cmap="gray")
    fig_num = fig_num+1
    colors = ("red", "green", "blue")
    for j in img_array[arr_grid_num]:
        histogram, bin_edges = np.histogram(j, bins=256, range=(0, 1))
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("grayscale value")
        plt.ylabel("pixel count")
        plt.xlim([0.0, 1.0])
        plt.plot(bin_edges[0:-1], histogram)
        fig_num = fig_num+1
    arr_grid_num = arr_grid_num+1

plt.show()

