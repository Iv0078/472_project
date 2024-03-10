# -*- coding: utf-8 -*-

# Ivan Balksnki ID:40151720


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

class_names = ['angry', 'fear', 'neutral', 'sad','suprise']
counts = [921, 970, 1186, 1198,737]


ax.bar(class_names, counts)

ax.set_ylabel('Number of images')
ax.set_title('Number of test images')


plt.show()