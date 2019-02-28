#视频分片
import os
import cv2

videoCapture = cv2.VideoCapture()

path = '/media/zzx/DATA/data/UCF-101/'
save_path = '/media/zzx/DATA/frames/'

folders = os.listdir(path)

for folder in folders:

    folder_dir = path + folder + '/'
    save_folder = save_path + folder
    os.mkdir(save_folder)
    videos = os.listdir(folder_dir)

    for video in videos:

        save_pics = save_folder + '/' + video[0:len(video)-3]
        #make the dir to store frames for this video
        os.mkdir(save_pics)
        videoCapture.open(folder_dir+video)
        frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

        for i in range(int(frames)):
            ret,frame = videoCapture.read()
            cv2.imwrite(save_pics +'/'+ video + '(%d).bmp'%i,frame)

        videoCapture.release()        
