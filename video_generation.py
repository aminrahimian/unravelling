import os
import cv2
from settings import *

file_dir= './data/visualizing-spread/fb100_edgelist_American75/output/'
img_array=[]

videowrite=cv2.VideoWriter(r'./data/visualizing-spread/fb100_edgelist_American75/output/video.mp4',-1,1,(396,396))  #定义保存视频目录名称及压缩格式，fps=1,像素为1280*720
for filename in [r'./data/visualizing-spread/fb100_edgelist_American75/output/{0}.png'.format(i) for i in range(80)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)
for i in range(80):  # Write all files into the video
    videowrite.write(img_array[i])
videowrite.release()
print('end!')
