from ultralytics import YOLO
from clearml import Task

task = Task.init(project_name="fire_and_smoke_detection", task_name="detection_v1")

# Load the model.
model = YOLO('weights/yolov8x.pt')
 
# Training.
results = model.train(
   data='Latest_Data/data.yaml',
   imgsz=640,
   epochs=20,
   batch=8,
   name='yolov8s_custom'
   )
