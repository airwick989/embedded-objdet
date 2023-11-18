import cv2
import time



start_time = time.time()

vidcapture = cv2.VideoCapture('traffic.mov')
classifierCar = cv2.CascadeClassifier('carsignatures.xml')
cars_counted = 0
VIDEO_LEN_FRAMES = 500  #Video is 17s at 30fps

for i in range(0, VIDEO_LEN_FRAMES):
    
    placeholder, frames = vidcapture.read()
    grayscale = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Perform detection of cars on screen for the single frame
    detected_cars = classifierCar.detectMultiScale(grayscale, 1.1, 1)
    cars_counted = len(detected_cars)
    print(f"Cars counted in current frame: {cars_counted}")

cv2.destroyAllWindows()
print(f"OBJECT DETECTION EXECUTION TIME: {time.time() - start_time} seconds")