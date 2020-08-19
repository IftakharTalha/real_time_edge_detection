
import cv2  
img = cv2.imread('test1.jpg')  

width =400
height=500

dsize = (height, width)

resize = cv2.resize(img,dsize,interpolation = cv2.INTER_AREA)


edges = cv2.Canny(resize,400,500)  

cv2.imshow("Original Image", img)  
cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Resize Image",resize)

cv2.waitKey(0)
cv2.destroyAllWindows()