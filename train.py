from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8s.pt')
 
# Training.
results = model.train(
   data='/home/emir/fire_detection/latest_data/data.yaml',
   imgsz=640,
   epochs=15,
   batch=8,
   name='yolov8s_custom'
   )
