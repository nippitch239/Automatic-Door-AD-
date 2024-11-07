# Object Detection with Inference API and Arduino Control

This project uses a computer vision model to detect objects in real-time from a webcam, sending commands to an Arduino based on detected classes. The program utilizes Roboflow's inference API for object detection and OpenCV for video capture.

## Features
main.py:
- Detects objects in real-time using Roboflow's inference API.
- Controls an Arduino based on specific object detections
- Supports threaded control for real-time input handling.
image.py:
- Image Processing: Processes multiple images from a folder and applies object detection to each one.

## Prerequisites

1. **Python>=3.8, <=3.11** installed.
2. **Libraries**:
   - `opencv-python`: for video capture and image handling.
   - `inference-sdk`: for communication with the inference API.
   - `pyserial`: for communication with the Arduino.
   - `ultralytics`: for YOLO model handling
3. **Roboflow Account**:
   - A Roboflow account with access to a model you can query via the inference API.
4. **Arduino**:
   - An Arduino connected to the computer via USB. Adjust the serial port as needed (`COM3` in the example).

## Installation

1. Install the required libraries:
   ```bash
   pip install opencv-python inference-sdk pyserial
2. Install all the dependencies with a single command:
   ```bash
   pip install -r requirements.txt