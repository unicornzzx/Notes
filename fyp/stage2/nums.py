import os

base = "F:\\frames"

video_types = os.listdir(base)
for video_type in video_types:
    type_path = os.path.join(base, video_type)
    video_names = os.listdir(type_path)

    for video_name in video_names:
        checking_path = os.path.join(type_path.replace("F:\\frames","C:\\new_UCF101"), video_name + ".avi")
        if not os.path.isfile(checking_path):
            print(video_name)