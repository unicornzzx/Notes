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
        self.sideLength=radius*2+1
    #Gaussian Function
    def calc(self,x,y):
        #权重的计算公式，xy为高斯模板中的点的坐标
        res1=1/(2*math.pi*self.sigema*self.sigema)
        res2=math.exp(-(x*x+y*y)/(2*self.sigema*self.sigema))
        return res1*res2
    
    #get Gassian template
    def template(self):
        #得出一个特定r,s值的高斯模板，只需计算一次就可以了
        print(self.radius)
        print(self.sigema)
        result = np.zeros((self.sideLength, self.sideLength))
        for i in range(self.sideLength):
            for j in range(self.sideLength):
                result[i,j]=self.calc(i-self.radius, j-self.radius)
        all=result.sum()
        return result/all
    

    def filter(self, image, mask, template):
        # mask is the segmentation mask that provides the position information of pixels that will be blured (an list)
        # image is the image that will be processed 
        # template is the Gassian template which will be used to blur the image
        new = np.array(image) #这里用两个nparray去存原图片的像素rgb信息
        raw = np.array(image) #是为了让先进行颜色替换的像素不会影响到其他像素求替换后的值
        maxRow = image.shape[0]-self.radius-1 #filter全在image内的px的最大行引索值
        maxColumn = image.shape[1]-self.radius-1 #filter全在image内的px的最大列引索值
        
        for position in mask:
            row = position[0]
            column = position[1]
            for k in range (3):
                t = np.zeros((self.sideLength, self.sideLength))
                if row < self.radius:#filter上方有几行px会定位在图片之外
                    if column < self.radius:#左 上
                        for i in range(self.radius - column):#filter前r-column列的px，列数为[0,r-column-1]
                            for j in range (sideLength):
                                if j < (self.radius - row):#行数为[0,r-row-1]的px
                                    #镜像
                                    t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                                else: #垂直轴对称 行数为[r-row,sideLength-1]的px
                                    t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                        for i in range(self.radius - column,sideLength):#filter第r-column列之后的px,列数为[r-column,sideLength-1]
                            for j in range (sideLength):
                                if j <(self.radius - row):#行数为[0,r-row-1]的px
                                    #水平轴对称
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                                else:#直接取  行数为[r-row,sideLength-1]的px
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                    elif column > maxColumn:#右 上
                        for i in range(sideLength - (column - maxColumn)):#px的列数为[0,sideLength-(column-maxColumn)-1]
                            for j in range (sideLength):
                                if j < (self.radius - row):#行数为[0,r-row-1]的px
                                    #水平轴对称
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                                else: #直接取
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                        for i in range(sideLength - (column - maxColumn),sideLength):#px的列数为[sideLength-(column-maxColumn),sideLength-1]
                            for j in range (sideLength):
                                if j <(self.radius - row):#行数为[0,r-row-1]的px
                                    #镜像
                                    t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                                else:#垂直轴对称
                                    t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                    else:# 仅上
                        for i in range(self.sideLength):
                            for j in range(self.sideLength):
                                if j < (self.radius - row):
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                                else:
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                    
                elif row > maxRow:#filter下方有几行px会定位在图片之外
                    if column < self.radius:#左 下
                        for i in range(self.radius - column):#filter前r-column列的px，列数为[0,r-column-1]
                            for j in range (sideLength):
                                if j < (sideLength - (row - maxRow)-1):#px的行数为[0,sideLength-(row-maxRow)-1]
                                    #垂直轴对称
                                    t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                                else: #镜像 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                    t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                        for i in range(self.radius - column,sideLength):#filter第r-column之后列的px,列数为[r-column,sideLength-1]
                            for j in range (sideLength):
                                if j <(sideLength - (row - maxRow)-1):#px的行数为[0,sideLength-(row-maxRow)-1]
                                    #直接取
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                else:#水平轴对称 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                    elif column > maxColumn:#右 下
                        for i in range(sideLength - (column - maxColumn)):#px的列数为[0,sideLength-(column-maxColumn)-1]
                            for j in range (sideLength):
                                if j <(sideLength - (row - maxRow)-1):#px的行数为[0,sideLength-(row-maxRow)-1]
                                    #直接取
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                else: #水平轴对称 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                        for i in range(sideLength - (column - maxColumn),sideLength):#px的列数为[sideLength-(column-maxColumn),sideLength-1]
                            for j in range (sideLength):
                                if j <(sideLength - (row - maxRow)-1):#px的行数为[0,sideLength-(row-maxRow)-1]
                                    #垂直轴对称
                                    t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                                else:#镜像 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                    else:#仅下
                        for i in range(self.sideLength):
                            for j in range(self.sideLength):
                                if j < (sideLength - (row - maxRow)-1):
                                    t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                else:
                                    t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                else:#filter全取在图像内
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