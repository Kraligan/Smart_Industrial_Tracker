# 📦 Smart Industrial Tracker

> Fine-tuned YOLOv11 model for object detection and productivity monitoring on a simulated production line.
![Demo Video](video/output.gif)

---

## Project Overview

**Smart Industrial Tracker** is a computer vision project designed to detect and count objects moving on a production line using a fine-tuned YOLOv11 model. This project demonstrates how computer vision can be used to automate industrial monitoring, track the efficiency of a process, and detect potential anomalies.

The goal is to build a fully functional object tracking pipeline capable of:

- Detecting objects in motion on a production line.
- Counting the total number of items processed.
- optionnaly raising alerts when objects stop or pile up (simulate quality check or error).
- Visualizing results in real time.

---

## Dataset & Source Video

- The training dataset is built by **extracting and annotating frames** from the following public video:
  **Source**: [Bottle Conveyor System (YouTube)](https://www.youtube.com/watch?v=K1KBXj7q_z0)

- Frames extracted with `ffmpeg` at 6 FPS
- Manual annotation is done using CVAT, exported in **YOLO format** and split into `train/val`.

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

4. **Visualization & Export**
   - Display real-time annotated video

---

## Lessons Learned

This project provided valuable hands-on experience with:

- **Dataset creation**: learning to extract and prepare high-quality frames for annotation.
- **Annotation strategy**: it’s **better to annotate full-resolution images** than resized (640x640), especially when working with **transparent objects** like glass bottles. Resizing before annotation makes small visual cues hard to see, even for a human annotator.
- **CVAT usage**: understanding how to organize annotation projects, define labels, and export YOLO-format data.
- **YOLOv11 fine-tuning**: how to train a model, adjust confidence thresholds, and interpret predictions.
- **Tracking limitations**: using `model.track()` with ByteTrack or DeepSORT is not well suited when objects are **visually identical**, as re-identification fails easily. In this case, a simple detection instead of tracking with ID was better.
- I now better understand **when to use detection vs. tracking**:
  - Use **tracking** when object appearance varies (e.g., people, vehicles).
  - Use **detection-only** when objects are identical and counting is enough.

---

## How to Use

Clone the project to your folder:
```bash
git clone https://github.com/Kraligan/Smart_Industrial_Tracker.git
```

Create virtual environment and Install requirements:
```bash
cd smart_industrial_tracker/
python3 -m venv venv
source venv/bin/active
pip install -r requirements.txt
```

Train the model:
```bash
python src/train.py
```

Run inference + counting:
```bash
python src/inf.py
```

---

## License & Credits

- **Model**: YOLOv11 by [Ultralytics](https://github.com/ultralytics/ultralytics)
  > This project is for **educational and non-commercial** use only.

- **Video**: Sourced from YouTube – all rights belong to the original creator.

- **Annotations, training, and tracking logic** developed by [Rémi Nollet](https://www.linkedin.com/in/remi-nollet/) as part of a personal showcase project.
