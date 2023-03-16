# -*- coding: utf-8 -*-
#%%
import cv2
import os

# 前三行 需要修改
j =  3  # --------设置初始的j  ------ 
while j < 42: # ------ 设置 结束的视频编号  -----
    file = 'f:\\coscopic\\B6\\B6-%d.avi'%(j)    # ---- 设置视频的地址 -----
    if os.path.exists(file) and not os.path.exists('%s_jpg'%(file)):
        vidcap = cv2.VideoCapture(file)
        
        #%% 获取总帧数
        total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        # 获取帧率
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        # 计算每个间隔多少帧
        arraysize = 20     #  ---------------这里设置的是矩阵的行数和列数 务必匹配---
        interval = total_frames // (arraysize - 1 ) # 产生多出一个图片        
        #%% ----------------     创建储存图片的文件夹
        directory = '%s_jpg'%file
        os.makedirs(directory)
        
        #%% 从头到尾每隔相等时间抽取总数20张图像
        for i in range(0, total_frames, interval):
           # 读取帧
           vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)  # 这段代码的作用是将vidcap对象的当前帧设置为指定的帧数i。这样，当vidcap.read()函数被调用时，它会读取从指定帧数开始的视频帧  
           success, image = vidcap.read()  # 从vidcap中读取一帧视频，并将其像素值存储在image中，同时返回一个布尔变量success，用于判断是否读取成功
           num = int((i / interval) + 1)
           re_num = arraysize + 1 - num
           # 如果读取成功则保存图像
           if success:
               filename = f"%s\\{num}-{re_num}.jpg"%(directory)
               cv2.imwrite(filename, image) 
    # break
    # 设置文件名称的步长
    j += 2    #  如果存在奇数偶数交叠  想要遍历每一个视频 可以改成 1 