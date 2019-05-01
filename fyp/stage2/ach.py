import os

ori_base = "C:\\new_UCF101"
new_base = "C:\\UCF101_NEW"

video_types = os.listdir(ori_base)
for video_type in video_types:
    ori_type_path = os.path.join(ori_base, video_type)
    new_type_path = os.path.join(new_base, video_type)
    if not os.path.isdir(new_type_path):
        os.makedirs(new_type_path)
    video_names = os.listdir(ori_type_path)
    for video in video_names:
        ori_path = os.path.join(ori_type_path, video)
        new_path = os.path.join(new_type_path,video)
        new_command = "ffmpeg -i "+ ori_path + " -b:v 500k -bufsize 500k -maxrate 1000k "+new_path
        os.system(new_command)