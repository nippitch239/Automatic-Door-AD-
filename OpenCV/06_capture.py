"Open Camera"
import cv2

capture = cv2.VideoCapture(0) # which camera (start with  index = 0)

while True :
    # 2 values (booleen, framerate)
    # first value is True if can read, false otherwise
    # second value is value from reading (first value have to be True)
    check, frame = capture.read() #read from camera (fps)
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("o") : # break when press "o" on keyboard
        break

#close window
capture.release()
cv2.destroyAllWindows()
