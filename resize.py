#import opencv library
import cv2
def resize(fname,width,height):  #function for resizing the image
    img=cv2.imread(fname)        #read the image
    cv2.imshow('Original image',img)  #display the image
    cv2.waitKey(0)  # delay
    org_height,org_width=img.shape[0:2] # retreiving the shape of the image
    print('height',org_height)
    print('width',org_width)
    if org_width >= org_height:  #resizing the width and height
        new_img=cv2.resize(img,(width,height))  
    else:
        new_img=cv2.resize(img,(height,width))
    return fname,new_img

resize('bird.jpg',1280,960)          #function call
