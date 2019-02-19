import os

frames_base = '/media/zzx/DATA/frames/'
processed_base = '/media/zzx/DATA/processed/'

total_types = 0
total_num = 0

video_types = os.listdir(frames_base)

for video_type in video_types:
    sum = 0 #这类视频中错误视频的个数
    list =  [] #错误视频的编号集合
    video_names = os.listdir(processed_base + '/' +video_type)
    for video_name in video_names:
        ori_len = len(os.listdir(frames_base + '/' +video_type + '/' + video_name + '.')
        len = len(os.listdir(processed_base + '/' +video_type + '/' + video_name)
        if (ori_len != len):
            list.append(video_name.split(_)[-2]+video_name.split(_)[-1])
            sum += 1
    if sum > 0:
        total_types += 1
        total_num += sum
        print(video_type + ': +\n' + list +'\n error number: ' + sum + '\n') #

print('the total number of error video types: ' + total_types)
print('the total number of error videos:' + total_num)
    

            