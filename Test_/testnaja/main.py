import cv2
from ultralytics import YOLO


model = YOLO("lp_detector.pt")
image = cv2.imread("test.jpg")
image = cv2.resize(image, (640, 480))
image_org = image.copy()


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = model(image_rgb)
boxes = results[0].boxes.xyxy.cpu().numpy()
for i, box in enumerate(boxes):
    x1, y1, x2, y2 = map(int, box)
    lp_img = image_org[y1:y2, x1:x2].copy()
    cv2.imshow(f"lp {i}", cv2.resize(lp_img, (560, 280)))
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, "license plate", (x1, y1), cv2.FONT_HERSHEY_COMPLEX,
                0.8, (255, 0, 255), 2) 

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
