
# 	coding: utf-8

# In[1]:

import cv2
import numpy as np
import copy

# In[7]:
im_base = cv2.imread("stinkbug.png",  cv2.IMREAD_GRAYSCALE)
im_morphed = cv2.imread("stinkbug_cloned.png",  cv2.IMREAD_GRAYSCALE)
im_mask = cv2.imread("stinkbug_cloned_mask.png", cv2.IMREAD_GRAYSCALE)

it = 10; # Set number of iterations


# In[ ]:




# In[ ]:

im_temp = cv2.imread("stinkbug_cloned.png",  cv2.IMREAD_GRAYSCALE)
im_seamless = im_temp
for a in range(it):
    for i in range(im_morphed.shape[0]):
        for j in range(im_morphed.shape[1]):
            if (im_mask[i,j]==255):
                im_temp[i,j]= 0.25*(im_seamless[i+1, j]+im_seamless[i-1, j]+im_seamless[i, j-1]+im_seamless[i, j+1]+ 4*im_morphed[i,j]-(im_morphed[i+1, j]+im_morphed[i-1, j]+im_morphed[i, j-1]+im_morphed[i, j+1]));
    im_seamless=im_temp;
    print a


# In[ ]:

cv2.imshow("Seamless Cloning", im_temp); cv2.waitKey(0); cv2.destroyAllWindows()


# In[ ]:



