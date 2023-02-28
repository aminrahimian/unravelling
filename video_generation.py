import glob
import os
from os.path import isfile, join
import cv2
from settings import *


def video_generation(path, output, fps, time):
    """
    :param path: Input file path
    :param output: Output file path
    :param fps: fps
    :param time: time to show
    :return: NONE
    """
    img_array = []
    for filename in [path + '{0}.png'.format(i) for i in range(25)]:
        img = cv2.imread(filename)
        # height, width, layers = img.shape
        size = (800, 800)
        for k in range(time):
            if img is None:
                print(filename + " is error!")
                continue
            img_array.append(img)
    videowrite = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(img_array)):
        videowrite.write(img_array[i])
    videowrite.release()

# Images path
path = './data/unraveling_example/figures/'
# Video path
output_path = path + 'video.avi'
# Value of fps
fps = 1
# Time for each of the figure
time = 1
video_generation(path, output_path, fps, time)

'''
# Codes used for unraveling example of real cases
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
'''
