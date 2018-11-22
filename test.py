# pink - [192,128,128,255]
import os
import math
import numpy as np
from PIL import Image
import time
from multiprocessing import Pool
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
        maxRow = raw.shape[0]-self.radius-1 #filter全在image内的px的最大行引索值
        maxColumn = raw.shape[1]-self.radius-1 #filter全在image内的px的最大列引索值
        
        for position in mask:
            row = position[0]
            column = position[1]
            for k in range (3):
                t = np.zeros((self.sideLength, self.sideLength))
                
                if row < self.radius:#filter上方有几行px会定位在图片之外
                    if column < self.radius:#左 上
                        for i in range(self.radius - column):#filter前r-column列的px，列数为[0,r-column-1]
                            for j in range(self.radius - row):
                                #镜像
                                t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                            for j in range(self.radius - row, self.sideLength):
                                #垂直轴对称 行数为[r-row,sideLength-1]的px
                                t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                        for i in range(self.radius - column,self.sideLength):#filter第r-column列之后的px,列数为[r-column,sideLength-1]
                            for j in range(self.radius - row):
                                #行数为[0,r-row-1]的px
                                #水平轴对称
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                            for j in range(self.radius - row, self.sideLength):
                                #直接取  行数为[r-row,sideLength-1]的px
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]                      

                    elif column > maxColumn:#右 上
                        for i in range(self.sideLength - (column - maxColumn)):#px的列数为[0,sideLength-(column-maxColumn)-1]
                            for j in range (self.radius - row):
                                #水平轴对称
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                            for j in range(self.radius - row,self.sideLength):#直接取
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                        for i in range(self.sideLength - (column - maxColumn),self.sideLength):#px的列数为[sideLength-(column-maxColumn),sideLength-1]
                            for j in range(self.radius - row):#行数为[0,r-row-1]的px
                                #镜像
                                t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                            for j in range(self.radius - row,self.sideLength):
                                #垂直轴对称
                                t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                                    
                    else:# 仅上
                        for i in range(self.sideLength):
                            for j in range(self.radius - row):
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]#水平轴对称
                            for j in range(self.radius - row,self.sideLength):#直接取
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                    
                elif row > maxRow:#filter下方有几行px会定位在图片之外
                    if column < self.radius:#左 下
                        for i in range(self.radius - column):#filter前r-column列的px，列数为[0,r-column-1]
                            for j in range (self.sideLength - (row - maxRow)):
                                #px的行数为[0,sideLength-(row-maxRow)-1]
                                #垂直轴对称
                                t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                            for j in range (self.sideLength - (row - maxRow),self.sideLength): #镜像 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                        for i in range(self.radius - column,self.sideLength):#filter第r-column之后列的px,列数为[r-column,sideLength-1]
                            for j in range (self.sideLength - (row - maxRow)):
                                #px的行数为[0,sideLength-(row-maxRow)-1]
                                #直接取
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                            for j in range (self.sideLength - (row - maxRow),self.sideLength):#水平轴对称 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                                
                    elif column > maxColumn:#右 下
                        for i in range(self.sideLength - (column - maxColumn)):#px的列数为[0,sideLength-(column-maxColumn)-1]
                            for j in range (self.sideLength - (row - maxRow)):
                                #px的行数为[0,sideLength-(row-maxRow)-1]
                                #直接取
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                            for j in range (self.sideLength - (row - maxRow),self.sideLength): #水平轴对称 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                        for i in range(self.sideLength - (column - maxColumn),self.sideLength):#px的列数为[sideLength-(column-maxColumn),sideLength-1]
                            for j in range (self.sideLength - (row - maxRow)):
                                #px的行数为[0,sideLength-(row-maxRow)-1]
                                #垂直轴对称
                                t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                            for j in range (self.sideLength - (row - maxRow),self.sideLength):#镜像 #px的行数为[sideLength-(row-maxRow),sideLength-1]
                                t[j][i]=raw[row+self.radius-j][column+self.radius-i][k]
                                
                    else:#仅下
                        for i in range(self.sideLength):
                            for j in range(self.sideLength - (row - maxRow)):
                                t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                            for j in range(self.sideLength - (row - maxRow),self.sideLength):
                                t[j][i]=raw[row+self.radius-j][column-self.radius+i][k]
                                    
                elif column < self.radius: #仅左
                    for i in range(self.radius - column):
                        for j in range(sideLength):
                            #垂直轴对称
                            t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                    for i in range(self.radius-column,self.sideLength):
                        for j in range(self.sideLength):
                            #直接取
                            t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                                         
                elif column > maxColumn: #仅右
                    for i in range(self.sideLength - (column - maxColumn)):
                        for j in range(self.sideLength):
                            #直接取
                            t[j][i]=raw[row-self.radius+j][column-self.radius+i][k]
                    for i in range(self.sideLength - (column - maxColumn),self.sideLength):
                        for j in range(self.sideLength):
                            #垂直轴对称
                            t[j][i]=raw[row-self.radius+j][column+self.radius-i][k]
                                    
                else:#filter全取在图像内
                    t = raw[row-self.radius:row+self.radius+1, column-self.radius:column+self.radius+1,k]

                a = np.multiply(t, template)
                new[row, column,k] = a.sum()
        newImage = Image.fromarray(new)
        return newImage

    def getMask(self,maskPath):
        f = open(maskPath,'rb')
        img = Image.open(f)
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
        f.close()
        return positions
        
if __name__=='__main__':
    r=7 #模版半径，自己自由调整
    s=50 #sigema数值，自己自由调整
    blur=Blur(radius=r, sigema=s)#声明高斯模糊类
    temp=blur.template()#得到滤波模版
    segmentation_base = '/media/zzx/DATA/segmentation/'
    frames_base = '/media/zzx/DATA/frames/'
    processed_base = '/media/zzx/DATA/processed/'
    video_types = os.listdir(segmentation_base)
    for video_type in video_types:
        video_names = os.listdir(segmentation_base + video_type + '/')
        for i in range(len(video_names)):
            p = Pool()
            video_name = video_names[i]
            video_name_f = video_name.split('.txt')[0]
            video_name_new = video_name.split('..txt')[0]
            mask_names = os.listdir(segmentation_base + video_type + '/' + video_name + '/')
                for j in range(len(mask_names)):
                    mask_name = mask_names[j]
                    frame_name = mask_name.split('_mask')+[0] + '.bmp'
                    f = open(frames_base + '/' + video_type + '/' + video_name_f + '/' + frame_name,'rb')
                    frame = Image.open(f)
                    mask = blur.getMask(segmentation_base + video_type + '/' + video_name + '/' + mask_name)
                    new = processed_base + '/' + video_type + '/' + video_name_new + '/' 
                    p.apply_async(blur.filter, args=(frame,mask,temp))
                    if not os.path.exists(new):
                        os.makedirs(new)
                    image.save(new + frame_name)
                    f.close()
                    print('generating---'+ new + frame_name)
            p.close()
            p.join()
            print('All images of type: '+video_name+' are produced.')
                