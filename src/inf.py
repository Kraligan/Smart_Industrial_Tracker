# imports
import cv2
import os
from ultralytics import YOLO
import torch

# Load model
model = YOLO("src/smart_industrial_tracker/bottle_finetune/weights/last.pt")

# Load video
video_path = os.path.expanduser("~/smart_industrial_tracker/video/input.mp4")
print(video_path)
cap = cv2.VideoCapture(video_path)

# Video writer
output_path = os.path.expanduser("~/smart_industrial_tracker/video/output.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# === Ligne verticale à x = 410
line_x = 410
total_count = 0

# Liste pour éviter de compter plusieurs fois le même objet par frame
counted_this_frame = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # === Predict with confidence threshold
    results = model.predict(frame, conf=0.5, verbose=False)[0]

    counted_this_frame = 0  # réinitialiser à chaque frame

    for box, conf in zip(results.boxes.xyxy.cpu().numpy(), results.boxes.conf.cpu().numpy()):
        x1, y1, x2, y2 = box
        cx = int((x1 + x2) / 2)

        # Détection de passage par la ligne verticale x = 410 (tolérance de 5 px)
        if line_x-2 < cx < line_x+2:
            counted_this_frame += 1

    total_count += counted_this_frame

    # === Annotate frame (classes + conf etc.)
    annotated_frame = results.plot()

    # === Afficher la ligne et le compteur
    cv2.line(annotated_frame, (line_x, 0), (line_x, frame.shape[0]), (0, 0, 255), 2)
    cv2.putText(annotated_frame, f"Count: {total_count}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show frame
    cv2.imshow("Tracking", annotated_frame)
    out.write(annotated_frame)

    # Quit on 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()