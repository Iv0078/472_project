# -*- coding: utf-8 -*-

# Ivan Balksnki ID:40151720


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

class_names = ['angry', 'fear', 'neutral', 'sad','suprise']
counts = [3849, 3835, 4884,4449,2990]


ax.bar(class_names, counts)

ax.set_ylabel('Number of images')
ax.set_title('Number of training images')


plt.show()