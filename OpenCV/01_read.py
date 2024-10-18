"Read Image"
import cv2

# read image
img = cv2.imread("OpenCV/image/car.jpg")

print(img) # numpy array of img
print(img.ndim) # dimension of numpy array