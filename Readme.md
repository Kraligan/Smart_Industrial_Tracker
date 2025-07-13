# 📦 Smart Industrial Tracker

> Fine-tuned YOLOv11 model for object tracking and productivity monitoring on a simulated production line.

---

## Project Overview

**Smart Industrial Tracker** is a computer vision project designed to track and count objects moving on a production line using a fine-tuned YOLOv11 model. This project demonstrates how computer vision can be used to automate industrial monitoring, track the efficiency of a process, and detect potential anomalies.

The goal is to build a fully functional object tracking pipeline capable of:

- Detecting objects in motion on a production line.
- Assigning persistent object IDs using tracking.
- Counting the total number of items processed.
- Raising alerts when objects stop or pile up (simulate quality check or error).
- Visualizing results in real time with a clear, user-friendly overlay.

---

## Dataset & Source Video

- The training dataset is built by **extracting and annotating frames** from the following public video:

  📹 **Source**: [Bottle Conveyor System (YouTube)](https://www.youtube.com/watch?v=K1KBXj7q_z0)

- Manual annotation is done using CVAT and exported in **YOLO format**.

---

## Main Steps

1. **Dataset Construction**
   - Extract video frames at regular intervals
   - Annotate objects (e.g. boxes, bottles, pieces) with bounding boxes
   - Split into train/val sets and export to YOLO format

2. **YOLOv11 Fine-Tuning**
   - Configure the dataset YAML
   - Fine-tune from a pretrained YOLOv11 base model
   - Evaluate model performance on validation set

3. **Tracking & Counting**
   - track objects with IDs.
   - Count unique objects crossing a predefined line
   - Monitor stopped or misaligned objects

4. **Visualization & Export**
   - Display real-time annotated video

---

## Results

To be added soon.

---

## ▶️ How to Use

Coming soon: setup instructions and example usage commands.

---

## License & Credits

- **Model**: YOLOv11 by [Ultralytics](https://github.com/ultralytics/ultralytics)
  > This project is for **educational and non-commercial** use only.

- **Video**: Sourced from YouTube – all rights belong to the original creator.

- **Annotations, training, and tracking logic** developed by [Rémi Nollet](https://www.linkedin.com/in/remi-nollet/) as part of a personal showcase project.
