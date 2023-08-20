from ultralytics import YOLO #install ultralytics using ##  pip install ultralytics  ##
model= YOLO("PATH TO label.pt")
results = model(source="SET TO 1 FOR WEBCAM OTHERWISE SET THE PATH TO DIRECTORY WITH YOUR IMAGES" , show = True , conf=0.3, save=True)
