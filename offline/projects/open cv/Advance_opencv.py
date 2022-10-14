import cv2

img = cv2.imread('img.jpg',1)
img = cv2.resize(img, (400,600))

# print(type(img))
print(img.shape)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()