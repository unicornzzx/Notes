# pink - [192,128,128,255]
import math
import numpy as np
from PIL import Image
import time
# a piece of code to get all path

class Blur():
    #initialization
    def __init__(self, radius=1, sigema=1.5):
        self.radius=radius
        self.sigema=sigema
    
    #Gaussian Function
    def calc(self,x,y):
        res1=1/(2*math.pi*self.sigema*self.sigema)
        res2=math.exp(-(x*x+y*y)/(2*self.sigema*self.sigema))
        return res1*res2
    
    #get Gassian template
    def template(self):
        print(self.radius)
        print(self.sigema)
        sideLength=self.radius*2+1
        result = np.zeros((sideLength, sideLength))
        for i in range(sideLength):
            for j in range(sideLength):
                result[i,j]=self.calc(i-self.radius, j-self.radius)
        all=result.sum()
        return result/all
    
    def filter(self, image, mask, template):
        new = np.array(image)
        raw = np.array(image)
        for position in mask:
            row = position[0]
            column = position[1]
            for k in range (3):
              t = raw[row-self.radius:row+self.radius+1, column-self.radius:column+self.radius+1,k]
              a = np.multiply(t, template)
              new[row, column,k] = a.sum()
        newImage = Image.fromarray(new)
        return newImage

    def getMask(self,maskPath):
      img = Image.open(maskPath)
      mask = np.array(img)
      #get the position of pixel whose rgb value == xxx
      height = mask.shape[0]
      width = mask.shape[1]
      positions = []
      for i in range(height):
        for j in range(width):
          rgb = mask[i][j]
          if rgb[0] == 192 and rgb[1] ==128 and rgb[2] == 128 and rgb[3] == 255:
            positions.append((i,j))
      return positions
        
time1 = time.time()
r=7 #模版半径，自己自由调整
s=50 #sigema数值，自己自由调整
blur=Blur(radius=r, sigema=s)#声明高斯模糊类
temp=blur.template()#得到滤波模版
im=Image.open('v_PlayingTabla_g01_c01.avi(0).bmp')#打开图片
poss = blur.getMask('v_PlayingTabla_g01_c01.avi(0)_mask.png')
image=blur.filter(im, poss, temp)#高斯模糊滤波，得到新的图片
image.show()#图片显示
time2 = time.time()
image.save('r=7 s=50.bmp')
print('二维卷积耗时:' + str(time2-time1))

    
    
