from ultralytics import YOLO
from clearml import Task

task = Task.init(project_name="fire_and_smoke_detection", task_name="detection_v1")

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
