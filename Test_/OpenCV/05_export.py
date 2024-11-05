"Export Image"
import cv2

# read image
img = cv2.imread("OpenCV/image/car.jpg",0)
resized_img = cv2.resize(img,(600,400))

# export image to output folder
cv2.imwrite("OpenCV/output/car-grey.jpg",resized_img)

#show image
cv2.imshow("Output",resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()