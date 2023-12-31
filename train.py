from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(data='datasets\data.yaml', epochs=150)