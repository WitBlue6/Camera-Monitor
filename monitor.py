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
    img1_arr = img1/255.0
    img2_arr = img2/255.0
    sum = np.sum(np.abs(img1_arr - img2_arr))
    if sum < threshold:
        return 0
    else:
        return 1

def camera_detact(capture, last_img=None):
    """
    检测一轮摄像机捕获有无变化
    :param last_img: 上一张图片
    :return: 当前图片
    """
    res = 0
    ret, frame = capture.read()
    img = np.array(frame[0])
    for i in range(args.noise):
        ret, frame = capture.read()
        img = np.array(frame[0])
        if not isinstance(last_img, np.ndarray):
            return img
        res += image_compare(img, last_img, threshold=args.threshold)
    if res >= args.noise // 2 + 1:
        t = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())  # 当前图片事件发生时间
        img_path = os.path.join(args.path, f'{t}.jpg')
        cv2.imwrite(img_path, frame)
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
    capture = cv2.VideoCapture(0)
    img = 0
    print(f'Monitor Start!\nParams:\nThreshold={args.threshold}, Period={args.period}, Noise={args.noise}\nSave Path:{args.path}')
    while True:
        print('\nBeginning Camera Capture...')
        if isinstance(img, np.ndarray):
            img = camera_detact(capture, last_img=img)
        else:
            img = camera_detact(capture)
        time.sleep(period)

# 参数调整
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--threshold', type=int, default=28)
parser.add_argument('--period', type=int, default=3)
parser.add_argument('--path', type=str, default='C:/Users/he/Desktop/camera')
parser.add_argument('--noise', type=int, default=5)
args = parser.parse_args()

if __name__ == '__main__':
    monitor(period=args.period)
    capture.release()              # 释放cap,销毁窗口
    cv2.destroyAllWindows()
