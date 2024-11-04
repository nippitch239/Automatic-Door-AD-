import cv2
from ultralytics import YOLO
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

model = YOLO("lp_detector.pt")

cap = cv2.VideoCapture("try.mp4")

if not cap.isOpened():
    print("ไม่สามารถเปิดไฟล์วิดีโอได้")
    exit()

target_width, target_height = 640, 480

while True:
    ret, frame = cap.read()
    if not ret:
        print("จบการอ่านวิดีโอ")
        break

    frame = cv2.resize(frame, (target_width, target_height))

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = model(frame_rgb)
    boxes = results[0].boxes.xyxy.cpu().numpy()

    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)
        lp_img = frame[y1:y2, x1:x2]

        lp_text = pytesseract.image_to_string(lp_img, config="--psm 8")

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, lp_text.strip(), (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX,
                    0.8, (255, 0, 255), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
