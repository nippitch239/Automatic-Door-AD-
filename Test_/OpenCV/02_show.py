"Show Image"
import cv2

# read image
img = cv2.imread("OpenCV/image/car.jpg")

#show image
cv2.imshow("Output",img)

cv2.waitKey(delay=5000) # auto close by delay times(ms)
cv2.waitKey(0) # always show
cv2.destroyAllWindows() # delete all windows