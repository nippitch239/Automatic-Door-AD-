"Resize Image"
import cv2

# read image
img = cv2.imread("OpenCV/image/car.jpg")

# resize
resized_img = cv2.resize(img,(600,400)) # (width, height)

#show image
cv2.imshow("Output",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()