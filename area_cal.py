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
count=0
for x in range(r.shape[0]):
  for y in range(r.shape[1]):
    val=r[x,y]
    if val>200:
      count=count+1
print(count)
all=r.shape[0]*r.shape[1]
potion=count/all
print(all)

h=0.8
w=h*width/height
all_area=h*w
red_area=all_area*potion
print(str(red_area)+'mm^2')
