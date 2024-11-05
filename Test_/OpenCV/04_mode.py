"Mode Image"
import cv2

# read image and mode
img = cv2.imread("OpenCV/image/car.jpg",1) # Color
img = cv2.imread("OpenCV/image/car.jpg",0) # Grey scale
img = cv2.imread("OpenCV/image/car.jpg",-1) # Alpha

resized_img = cv2.resize(img,(600,400))

#show image
cv2.imshow("Output",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()