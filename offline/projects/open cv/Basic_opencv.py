import cv2

img = cv2.imread('img.jpg',-1)      #Reading the image

#resizeing the image
img1 = cv2.resize(img,(500,700))    
#Another way to resize# AND #The second argument should always be (0,0)
img2 = cv2.resize(img,(0,0),fx=0.1,fy=0.1)  
#Resize half of its own size
img3 = cv2.resize(img,( int(img.shape[1]/8), int(img.shape[0]/8) )) 


#Rotating the image
img4 = cv2.rotate(img2, cv2.ROTATE_90_COUNTERCLOCKWISE)   

#It saves all your changes with a new image
#cv2.imwrite('Rotate_image.jpg',img4)    


cv2.imshow('Image',img4)    #showing the image
cv2.waitKey(0)              #wait until any key is pressed
cv2.destroyAllWindows()     #close all the windows
