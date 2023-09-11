import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture("videoplayback_2.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

model = YOLO("best_trained.pt")

detection_classes = {0:"fire",1:"smoke"}

while cap.isOpened():
    _, frame = cap.read()
    result = model(frame,stream=True)
    for info in result:
        boxes= info.boxes
        for box in boxes:
            class_=detection_classes[int(box.cls[0])]
            print(list(box.cls))
            confidence = box.conf[0]
            confidence = int(confidence*100)
            
            if confidence > 10:
                    x1, y1, x2, y2 = box.xyxy[0]

                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),4)

                    cv2.putText(frame, f"{confidence}%:{class_}",(x1+4,y1+100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
                    out.write(frame)
            else:
                 out.write(frame)
            cv2.imshow("Frames",frame)
            cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()


