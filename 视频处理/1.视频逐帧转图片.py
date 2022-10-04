# 使用这篇代码将视频逐帧分割
import cv2
import os


def save_img(video_path, pic_dir):
    os.makedirs(pic_dir, exist_ok=True)
    vc = cv2.VideoCapture(video_path)
    c = 0
    rval = vc.isOpened()
    while rval:
        c += 1
        rval, frame = vc.read()
        pic_path = pic_dir
        if rval:
            cv2.imwrite(pic_path + str(c) + '.jpg', frame)
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success')


if __name__ == '__main__':
    video_path = "D:/Desktop/11.mp4"  # 源视频的路径
    pic_dir = "D:/Desktop/pic/"  # 图片保存目录，一定要以 '/' 结尾
    save_img(video_path, pic_dir)
