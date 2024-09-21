import cv2
import numpy as np
import pandas as pd
import time
import argparse
import os

def image_compare(img1, img2, threshold=100):
    """
    RGB图比较
    :param img: 640x3 np.ndarray
    :return:若两图片无较大变化，返回false
    """
    img1_arr = cv2.GaussianBlur(img1, (5, 5), 0) / 255.0
    img2_arr = cv2.GaussianBlur(img2, (5, 5), 0) / 255.0
    sum = np.sum(np.abs(img1_arr - img2_arr))
    print('Difference Score:'+str(sum))
    if sum < threshold:
        return False
    else:
        return True

def camera_detect(capture, last_img=None):
    """
    检测一轮摄像机捕获有无变化
    :param last_img: 上一张图片
    :return: 当前图片
    """
    frames = []
    for i in range(args.noise): # 时间平均处理
        ret, frame = capture.read()
        if ret:
            frames.append(np.array(frame))
    frame_avg = np.mean(frames, axis=0)
    img = frame_avg[0]
    if not isinstance(last_img, np.ndarray):
        return img
    res = image_compare(img, last_img, threshold=args.threshold)
    if res:
        t = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())  # 当前图片事件发生时间
        img_path = os.path.join(args.path, f'{t}.jpg')
        cv2.imwrite(img_path, frame_avg.astype('uint8'))
        print(f'Capture Writing at time:{t}')
        return img
    else:
        return last_img
def monitor(period=5):
    """
    监视程序入口
    :param period: 监视周期（秒）
    :return:
    """
    img = 0
    print(f'Monitor Start!\nParams:\nThreshold={args.threshold}, Period={args.period}, Noise={args.noise}\nSave Path:{args.path}')
    while True:
        capture = cv2.VideoCapture(0)
        if not capture.isOpened():
            print('#############ERROR##############\nCamera Has Been Closed!')
            exit(1)
        print('\nBeginning Camera Capture...')
        if isinstance(img, np.ndarray):
            img = camera_detect(capture, last_img=img)
        else:
            img = camera_detect(capture)
        capture.release()
        time.sleep(period)

# 参数调整
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--threshold', type=int, default=12)
parser.add_argument('--period', type=int, default=3)
parser.add_argument('--path', type=str, default='C:/Users/he/Desktop/camera')
parser.add_argument('--noise', type=int, default=5)
args = parser.parse_args()

if __name__ == '__main__':
    monitor(period=args.period)
    capture.release()              # 释放cap,销毁窗口
    cv2.destroyAllWindows()
