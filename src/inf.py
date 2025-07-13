# imports
import cv2
import os
from ultralytics import YOLO

# Load model
model = YOLO("smart_industrial_tracker/bottle_finetune/weights/last.pt")

# Load video
video_path = os.path.expanduser("~/Smart_Industrial_Tracker/video/input.mp4")
print(video_path)
cap = cv2.VideoCapture(video_path)

# Video writer
output_path = os.path.expanduser("~/Smart_Industrial_Tracker/video/output.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Inference loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Tracking with YOLOv11
    results = model.track(frame, persist=True, verbose=False)

    # Plot results on frame
    annotated_frame = results[0].plot()

    # Show frame
    cv2.imshow("Tracking", annotated_frame)
    out.write(annotated_frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()