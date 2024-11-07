from ultralytics import YOLO
import cv2
import os

model = YOLO('model.pt')
folder_path = 'img'

for image_name in os.listdir(folder_path):
    image_path = os.path.join(folder_path, image_name)


    img = cv2.imread(image_path)
    

    if img is None:
        print(f"Could not read {image_path}. Skipping.")
        continue

    results = model.predict(source=img, imgsz=640)
    for result in results:
        frame = result.plot()
        cv2.imshow('YOLO Detection', frame)
        if cv2.waitKey(0) == 6:
            break

cv2.destroyAllWindows()
