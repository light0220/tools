# 使用这篇代码提取声音
from moviepy.editor import *
import os

video_path = './练习文件/视频处理/视频源/' # 保存视频的路径
video_name = os.listdir(video_path)[0] # 视频的名字
os.makedirs('./练习文件/视频处理/音频输出/', exist_ok=True)

video = VideoFileClip(video_path + video_name)  #保存视频的路径
audio = video.audio
audio.write_audiofile('./练习文件/视频处理/音频输出/audio.mp3')