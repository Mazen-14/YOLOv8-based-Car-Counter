from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
from names import classNames

#cap = cv2.VideoCapture(0)
#cap.set(3, 1280)
#cap.set(4, 720)

cap = cv2.VideoCapture("../Videos/cars.mp4")

model = YOLO("../Yolo/yolov8n.pt")

mask = cv2.imread("../Photos/mask.png")

# Tracking
tracker = Sort(max_age=20,min_hits=3,iou_threshold=0.3)

counter = []
last_id=0

while True:

    success, img = cap.read()
    ImgRegion = cv2.bitwise_and(img,mask)

    imgGraphics = cv2.imread("../Photos/graphics.png", cv2.IMREAD_UNCHANGED)
    imgGraphics = cv2.resize(imgGraphics, (200, 100))
    img = cvzone.overlayPNG(img,imgGraphics,(0,0))

    results = model(ImgRegion ,stream = True )
    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1 ,y1 ,x2 ,y2 = box.xyxy[0]
            x1, y1 ,x2,y2 = int(x1), int(y1),int(x2), int(y2)
            w , h = x2 - x1, y2 - y1
            w , h = int(w) , int(h)
            bbox = x1,y1,w,h
            print(x1, y1, w, h)

            # Confidence
            conf = math.ceil((box.conf[0]*100))/100

            # Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass == 'car' and conf > 0.3:
                cvzone.cornerRect(img, bbox, l=20,colorR=(255,0,0),colorC=(255,255,50),rt=1)
                #cvzone.putTextRect(img, f"{currentClass} {conf}", (max(0,int(x1)), max(40,int(y1))),scale=1,thickness=1)
                currentArray = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections,currentArray))

    resultsTracker = tracker.update(detections)

    #Line
    limits = [70, 300, 320, 320]
    cv2.line(img,(limits[0],limits[1]),(limits[2],limits[3]),(0,0,255),thickness=5)

    for result in resultsTracker:
        x1,y1,x2,y2,id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        w, h = int(w), int(h)
        bbox = x1,y1,w,h
        #cvzone.cornerRect(img, bbox, l=20)
        #cvzone.putTextRect(img, f"{int(id)}", (max(0, int(x1)), max(40, int(y1))), scale=1, thickness=1)

        print(result)

        cx , cy = x1+w//2 , y1+h//2
        cv2.circle(img,(cx,cy),2,(255,255,0),cv2.FILLED)
        if limits[0]<cx<limits[2] and limits[1]-20<cy<limits[3]+20 :
            if counter.count(id) == 0:
                counter.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), thickness=5)

        #cvzone.putTextRect(img, f"Count : {len(counter)}",( 50,50), scale=2, thickness=3)
        cv2.putText(img, str(len(counter)), (110, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 50, 50), 3)

    cv2.imshow('Image',img)
    #cv2.imshow('ImageRegion',ImgRegion)
    cv2.waitKey(1)