import cv2
import numpy as np 

def rotate_and_flip_image(image_path):
    
    img = cv2.imread(image_path)
    
    center = (img.shape[1]//2,img.shape[0]//2)
    
    M = cv2.getRotationMatrix2D(center, 45, 1)
    
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    
    
    nW = int((img.shape[0]*sin)+ (img.shape[1]*cos))
    nH = int((img.shape[0]*cos)+ (img.shape[1]*sin))
    
    M[0,2] += (nW/2) - center[0]
    M[1,2] += (nH/2) - center[1]

    rotated_img = cv2.warpAffine(img, M, (nW,nH))
    
    mirrored_img = cv2.flip(rotated_img,-1)

    return mirrored_img

image_path = "watercolor-5049980_640.jpg"

mirrored_img = rotate_and_flip_image(image_path)

cv2.imwrite('mirrored_img.jpg',mirrored_img)
cv2.imshow("Mirrored Image", mirrored_img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
