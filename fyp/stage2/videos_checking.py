import os

ori_base = "F:\\frames"
new_base = "C:\\new_UCF101"

video_types = os.path.listdir(ori_base)
for video_type in video_types:
    lost_videos = []
    good_nums = 0

    ori_type_path = os.path.join(ori_base, video_type)
    new_type_path = os.path.join(ori_base, video_type)
    video_names = os.path.listdir(ori_type_path)

    for video_name in video_names:
        checking_path = os.path.join(new_type_path, video_name + ".avi")
        if os.path.isfile(checking_path):
            good_nums += 1
        else:
            lost_videos.append(checking_path)
    
    if len(lost_videos) != 0:
        print("Lost videos:---------------" + str(lost_videos))
    else:
        print("Done: " + video_type)
        print("Generated video numbers: "+ str(good_nums))
