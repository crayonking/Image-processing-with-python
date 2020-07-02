import cv2
def blur(img):   #defines function to blur the image
   kernels=[3,5,9,13]   #set the different kernel sizes
   for idx,k in enumerate(kernels):  
        img_blur=cv2.blur(img,ksize=(k,k))
        cv2.imshow(str(k),img_blur)  #display the image
        cv2.waitKey(0)
   return
