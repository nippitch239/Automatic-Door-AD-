import cv2
from inference_sdk import InferenceHTTPClient
import tempfile
import os
import threading
import serial

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="KEY"
)

ser = serial.Serial('COM3', 9600)
ser.flush()

running = True

def process_frame(frame):
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
        cv2.imwrite(temp_file.name, frame)
        temp_file_path = temp_file.name
    result = CLIENT.infer(temp_file_path, model_id="thai-lnpr-c6prf/3")
    os.remove(temp_file_path)
    return result
def main():
    global running
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit the application.")
    
    while running:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break
        result = process_frame(frame)
        
        if 'predictions' in result:
            classes_detected = [prediction['class'] for prediction in result['predictions']]
            print("Detected classes:", classes_detected)
            if "Bangkok" in classes_detected:
                ser.write(bytes([1]))
            elif "2" in classes_detected:
                ser.write(bytes([2]))
            if "" in classes_detected:
                ser.write(bytes([0]))
    cap.release()
    ser.close()

def check_for_exit():
    global running
    while running:
        if input() == 'q':
            running = False

if __name__ == "__main__":
    threading.Thread(target=check_for_exit, daemon=True).start()
    main()
