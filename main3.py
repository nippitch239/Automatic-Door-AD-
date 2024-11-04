import cv2
import numpy as np
from inference_sdk import InferenceHTTPClient
import tempfile
import os
import threading
import serial  # Import the serial library

# Initialize the inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="KEY"
)

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino port
ser.flush()

# Variable to control the running state of the application
running = True

def process_frame(frame):
    # Create a temporary file to store the frame
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
        # Write the frame to the temporary file
        cv2.imwrite(temp_file.name, frame)
        temp_file_path = temp_file.name

    # Perform inference using the temporary file
    result = CLIENT.infer(temp_file_path, model_id="thai-lnpr-c6prf/3")

    # Clean up the temporary file
    os.remove(temp_file_path)

    return result

def main():
    global running
    # Open the webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Press 'q' to quit the application.")
    
    while running:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Process the frame with the inference client
        result = process_frame(frame)
        
        # Extract and print the class from the result
        if 'predictions' in result:
            classes_detected = [prediction['class'] for prediction in result['predictions']]
            print("Detected classes:", classes_detected)  # Print detected classes

            # Check for the specific class "Bangkok"
            if "Bangkok" in classes_detected:
                ser.write(bytes([1]))  # Send binary command to Arduino to turn left
            elif "2" in classes_detected:
                ser.write(bytes([2]))  # Send binary command to turn right
            if "" in classes_detected:
                ser.write(bytes([0]))
    # Release the webcam
    cap.release()
    ser.close()  # Close the serial connection

def check_for_exit():
    global running
    while running:
        if input() == 'q':
            running = False

if __name__ == "__main__":
    # Start the exit check in a separate thread
    threading.Thread(target=check_for_exit, daemon=True).start()
    main()
