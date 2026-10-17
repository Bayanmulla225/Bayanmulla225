"""YOLO26 Webcam Object Detection"""

import cv2
from ultralytics import YOLO

# 1. Load the pretrained YOLOv8 nano model
model = YOLO("best_.pt")

# 2. Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open the webcam.")

print("Press 'q' in the video window to quit.")

try:
    while True:
        # 3. Read one image (frame) from the webcam
        success, frame = cap.read()

        if not success:
            print("Could not read a frame.")
            break

        # Run YOLO inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLO Webcam Detection", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()