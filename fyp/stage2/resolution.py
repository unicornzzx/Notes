import os
import cv2
import numpy as np

base = "F:\\processed"
bad = 0


video_types = os.listdir(base)
for video_type in video_types:
    type_path = os.path.join(base, video_type)
    video_names = os.listdir(type_path)

    for video_name in video_names:
        video_path = os.path.join(type_path, video_name)
        frames = os.listdir(video_path)
        max_num = 0
        for frame in frames:
            num = frame.split("avi(")[1].split(")")[0]
            numm = int(num)
            if numm > max_num:
                max_num = numm
        if len(frames) != max_num + 1 :
            print(video_name + "-------------------------"+ str(max_num +1 - len(frames)))
            bad += 1

print(bad)
            





