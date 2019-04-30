# generated blured ucf101 video dataset by processed frames

import os
import cv2
import time
from multiprocessing import Pool

def proc(video_type):
    frames_base = "F:\\processed"
    output_base = "C:\\new_UCF101"

    print("Staring:-----------------------" + video_type)
    video_names = os.listdir(os.path.join(frames_base, video_type))
    output_type_path = os.path.join(output_base,video_type)
    os.makedirs(output_type_path)

    for video_name in video_names:
        time1 =time.time()
        frames_folder = os.path.join(frames_base, video_type, video_name)
        frames = os.listdir(frames_folder) #此方法生成的list并不是按照帧的顺序

        fps = 25
        size = (320,240)
        video_name = frames_folder.split("\\")[-1] + ".avi"
        output_path = os.path.join(output_type_path, video_name) 
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        video_writer = cv2.VideoWriter(output_path, fourcc, fps, size)

        for i in range(len(frames)):
            frame_name = os.path.join(frames_folder, video_name + "(" + str(i) + ").bmp")
            frame = cv2.imread(frame_name)
            video_writer.write(frame)
        video_writer.release()

        time2 =time.time()
        print("Generated:  " + output_path +"------used time: "+ str(time2-time1))

if __name__ == '__main__':
    frame_base = "D:\\processed"
    video_types = os.listdir(frame_base)
    p = Pool(10)
    p.map(proc, video_types)
    p.close()
    p.join()