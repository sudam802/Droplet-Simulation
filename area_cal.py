import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read the image
image = cv2.imread('final.png')[315:451,550:670]
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
r=image[:,:,2]

width=r.shape[0]
height=r.shape[1]
print(r.shape)
