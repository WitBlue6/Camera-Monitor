# Camera-Monitor
摄像头监视脚本，若检测到摄像头画面有较大变化，保存一次捕获图片
# 使用方法
## 1.命令行前往下载目录  
```
cd E:/the/path/you/download/
```
## 2.运行脚本  
默认参数threshold=12, period=3, path=C:/Users/he/Desktop/camera, noise=5
```
python monitor.py --threshold=30 --period=3 --path=C:/Users/he/Desktop/camera --noise=7
```
## 3.参数说明  
threshold:摄像头捕获到的画面变化量阈值，阈值越小越敏感  
period:摄像头捕获周期，单位秒  
path:捕获图片保存路径  
noise:时间平均处理图片的个数，noise越大平均的图片越多

待改进：提高局部识别能力，引入YOLO网络

# 更新日志
2024-9-21  
1.修改摄像头开启关闭的逻辑，将常亮的工作状态改为闪烁工作  
2.将多次比较改为对图片进行时间平均处理，并添加高斯滤波减少噪声

2024-9-20  
1.添加在比较前检测摄像头是否开启的操作

2024-9-19  
1.添加抗干扰操作，在一段时间内连续比较，有半数以上的图片检测到变化时，保存捕获  
2.将灰度图比较改为RGB图比较
