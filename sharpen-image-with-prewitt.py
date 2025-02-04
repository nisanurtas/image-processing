import cv2
import numpy as np

def sharpen_image_with_prewitt(image_path):
    # Load the image in grayscale
    img = cv2.imread(image_path)
    
    # Reduce noise by blurring the image
    blur = cv2.GaussianBlur(img, (3,3), 0)
    
    # Prepare Prewitt edge detection masks
    kernelx = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
    kernely = np.array([[1,0,-1], [1,0,-1], [1,0,-1]])
    
    # Apply Prewitt operator in x and y directions
    prewitt_x = cv2.filter2D(blur, -1, kernelx)
    prewitt_y = cv2.filter2D(blur, -1, kernely)
    
    # Combine edges
    prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)
    
    # Sharpen the image
    sharpened = cv2.addWeighted(img, 1.5, prewitt, -0.5, 0)
    
    return sharpened


#file path
image_path = 'Blurring.jpeg'
sharpened_image_with_prewitt = sharpen_image_with_prewitt(image_path)


#save results
cv2.imwrite('sharpened_image_prewitt.png', sharpened_image_with_prewitt)
