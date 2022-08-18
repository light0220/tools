from winsound import PlaySound
import winsound
import cv2
import os
i = 1
cv2.namedWindow('image',0)
cv2.resizeWindow('image',1280,720)   #这两行用来创建大小可调的窗口，1280和720就是大小
au = r"./练习文件/视频处理/音频输出/audio.wav"
os.system(au)
PlaySound(au,winsound.SND_ASYNC)  # 这3行用来播放声音。

while True:
    try:
        img = cv2.imread('./pic/'+str(i)+'.jpg', 0)
        blur = cv2.GaussianBlur(img, (3, 3), 0) 
        canny = cv2.Canny(blur, 50, 150)
        #vid.write(canny)
        cv2.imshow('image',canny)
        cv2.waitKey(16)  # 播放每一帧的间隔。 由于每一帧都需要计算且计算量不同，所以间隔和电脑性能有关系。
        i += 1
        print(i) # 显示当前播放到第几帧
    except Exception:
        break
cv2.destroyAllWindows()









