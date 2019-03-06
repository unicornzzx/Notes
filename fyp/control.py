#使用训练好的deeplab模型来对目标目录下的图片进行批量语义分割

import os

list_dir = '/home/zzx/lists/'
#dataset_dir = '/media/zzx/DATA/frames/'

types = os.listdir(list_dir)[0:1] #get the video type names

for t in types:
    type_dir = list_dir+t+'/' #get the type path
    videos = os.listdir(type_dir) #get the video names
    videos_dirs = [os.path.join.(type_dir,video) for video in videos]#convert the list of video text file name to the list of their path
    for video in videos_dirs:
        os.system('python inference.py --infer_data_list '+video)
