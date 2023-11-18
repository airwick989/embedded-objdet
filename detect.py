import cv2
import numpy as np
import time



start_time = time.time()

vidcapture = cv2.VideoCapture('../traffic.mov')
classifierCar = cv2.CascadeClassifier('carsignatures.xml')
cars_counted = 0
VIDEO_LEN_FRAMES = 500  #Video is 17s at 30fps

for i in range(0, VIDEO_LEN_FRAMES):
    
    placeholder, frames = vidcapture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Perform detection of cars on screen for the single frame
    cars = classifierCar.detectMultiScale(gray, 1.1, 1)
    cars_counted = len(cars)
    print(f"Cars counted in current frame: {cars_counted}")

cv2.destroyAllWindows()

print(f"Cars counted: {cars_counted}")
print(f"OBJECT DETECTION EXECUTION TIME: {time.time() - start_time} seconds")