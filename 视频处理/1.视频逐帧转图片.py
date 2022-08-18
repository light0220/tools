# 使用这篇代码将视频逐帧分割
import cv2
import os
def save_img():
    video_path = './练习文件/视频处理/视频源/' # 保存视频的路径
    video_name = os.listdir(video_path)[0] # 视频的名字
    file_name = video_name.split('.')[0]
    os.makedirs('D:/Desktop/pic/', exist_ok=True)
    vc = cv2.VideoCapture(video_path+'/'+video_name)
    c=0
    rval=vc.isOpened()
    while rval:
        c = c + 1
        rval, frame = vc.read()
        pic_path = 'D:/Desktop/pic/'
        if rval:
            cv2.imwrite(pic_path + str(c) + '.jpg', frame)
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success')
    print(file_name)

    
save_img()