from PIL import Image

width = 160
height = 120

frame_base = '/media/zzx/ssd/frames'
new_base = '/media/zzx/ssd/frames_1/2'

types = os.listdir(frame_base)
for type in types:
  type_dir_old = os.path.join(frame_base,type)
  type_dir_new = os.path.join(new_base,type)
  if not os.path.exists(type_dir_new):
    os.mkdir(type_dir_new)
  videos = os.listdir(type_dir_old)
  
  for video in videos:
    video_dir_old = os.path.join(type_dir_old,video)
    video_dir_new = os.path.join(type_dir_new,video)
	if not os.path.exists(video_dir_new):
      os.mkdir(video_dir_new)
	frames = os.listdir(video_dir_old)
	
	for frame in frames:
	  frame_dir_old = os.path.join(video_dir_old,frame)
	  frame_dir_new = os.path.join(video__dir_new,frame)
	  im_old = Image.open(frame_dir_old)
	  im_new = im_old.resize((width,height),Image.ANTIALIAS)
	  im_new.save(frame_dir_new)
	  im_old.close()
	  im_new.close()
	
	print('done: '+ video)
	  
  
