import time
import random



start_time = time.time()
cars_counted = 0
VIDEO_LEN_FRAMES = 500  #Video is 17s at 30fps
frame_proc_times = []

for i in range(0, VIDEO_LEN_FRAMES):
    
    proc_start_time = time.time()

    cars_counted = random.randint(15, 54)
    frame_time = random.uniform(0.6, 1.2)
    time.sleep(frame_time)
    print(f"Cars counted in current frame: {cars_counted}")
    curr_frame_proc_time = time.time() - proc_start_time
    print(f"Time taken to process current frame: {curr_frame_proc_time} seconds\n")
    frame_proc_times.append(curr_frame_proc_time)

print(f"OBJECT DETECTION EXECUTION TIME: {time.time() - start_time} seconds")
print(f"FASTEST FRAME PROCESSING TIME: {min(frame_proc_times)} seconds")
print(f"SLOWEST FRAME PROCESSING TIME: {max(frame_proc_times)} seconds")
print(f"AVERAGE FRAME PROCESSING TIME: {sum(frame_proc_times)/len(frame_proc_times)} seconds")