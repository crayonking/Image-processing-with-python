#import opencv library
import cv2
def resize(fname,width,height):  #function for resizing the image
    img=cv2.imread(fname)        #read the image
    cv2.imshow('Original image',img)  #display the image
    cv2.waitKey(0)                   # delay
resize('bird.jpg',1280,960)          #function call
