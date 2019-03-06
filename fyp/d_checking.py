from PIL import Image
import os
from multiprocessing import Pool

def func(t):
  root = '/media/zzx/DATA1/frames/'
  videos = os.listdir(os.path.join(root, t))
  for video in videos:
    frames = os.listdir(os.path.join(root, t, video))
    for frame in frames:
      if (frame.endswith('.bmp')):
        try:
          im = Image.open(os.path.join(root, t, video, frame))
        except Exception as e:
          print('Damaged file:', os.path.join(root,t,video,frame))
  print('Finished: '+ t)

if __name__ == '__main__':
  
  root = '/media/zzx/DATA1/frames/'
  types = os.listdir(root)
  p = Pool(12)
  p.map(func, types)
  p.close()
  p.join()
