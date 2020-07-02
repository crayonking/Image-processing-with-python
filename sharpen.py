import cv2
import numpy as np
def sharp(img):
  kernel=np.array([[0,-1,0],[-1,5,-1],[0-1,0]])
  new_img=cv2.filter2D(img,-1,kernel)
  cv2.imshow('sharpened',new_img)
  cv2.waitKey(0)
  return new_img
