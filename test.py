from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')

# result = model(source="rtsp://raspberrypi.local:8554/MyStreamName", show=True, conf=0.4)
result = model(source="John Wick 3_ Gun Selection Scene _ HD.mp4", show=True, conf=0.4)