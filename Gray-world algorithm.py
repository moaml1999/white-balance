""" White balancing images using Gray-world algorithm 
he Gray World Assumption is a white balance method that assumes that your scene, on average, is a neutral gray. 
Gray-world assumption hold if we have a good distribution of colors in the scene. 
Assuming that we have a good distribution of colors in our scene,the average reflected color is assumed to be the color of the light.
 Therefore, we can estimate the illumination color cast by looking at the average color and comparing it to gray.  
Gray world algorithm produces an estimate of illumination by computing the mean of each channel of the image.

"""
import numpy as np 
import cv2
import sys 

img = cv2.imread("cat.jpg")

def GW_balance(img):
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    avg_a = np.average(img_lab[:,:,1])
    avg_b = np.average(img_lab[:,:,2])

    img_lab[:,:,1] = img_lab[:,:,1] - ((avg_a - 128) * (img_lab[:,:,0]/ 255.0) * 1.2)
    img_lab[:,:,2] = img_lab[:,:,2] - ((avg_b - 128) * (img_lab[:,:,0]/ 255.0) * 1.2)

    balance_img = cv2.cvtColor(img_lab, cv2.COLOR_LAB2BGR)
    return balance_img
    
GW_balance_img =  GW_balance(img)
cv2.imwrite("GW_Balance.jpg",GW_balance_img )

cv2.imshow("image", GW_balance_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

