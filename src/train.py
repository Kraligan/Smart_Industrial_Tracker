from ultralytics import YOLO

# === Configuration ===
MODEL_PATH = "yolov11.pt"
DATA_CONFIG = "data.yaml"
IMG_SIZE = 640
EPOCHS = 50
BATCH_SIZE = 16
PROJECT_NAME = "smart_industrial_tracker"
RUN_NAME = "bottle_finetune"

# === Training ===
if __name__ == "__main__":
    model = YOLO(MODEL_PATH)

    model.train(
        data=DATA_CONFIG,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        project=PROJECT_NAME,
        name=RUN_NAME,
        exist_ok=True,
        patience=5,              # early stopping
        verbose=True
    )