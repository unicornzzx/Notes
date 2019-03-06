import os
 
frames_base = '/media/zzx/ssd/frames' #两个需要比较的目录
segmentation_base = '/media/zzx/ssd/segmentation'

f = open('add_list.txt', mode = 'w')

video_types = os.listdir(frames_base)

for video_type in video_types:
    video_names = os.listdir(os.path.join(frames_base ,video_type))
    for video_name in video_names:
        frames = os.listdir(os.path.join(frames_base,video_type,video_name))
        masks = os.listdir(os.path.join(segmentation_base,video_type,video_name))
        if (len(frames) != len(masks)):
            for frame in frames:
                frame = os.path.join(frames_base, video_type, video_name, frame)
                mask = os.path.join(segmentation_base, video_type, video_name, frame)
                if not os.path.exist(mask):
                    f.write(frame)
                    f.next()
                    print('--------Add: '+ frame)
            print('Done: '+ video_name)        

f.close()
