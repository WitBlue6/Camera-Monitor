# Camera-Monitor
摄像头监视脚本，若检测到摄像头画面有较大变化，保存一次捕获图片
# 使用方法
## 1.命令行前往下载目录  
```
cd E:/the/path/you/download/
```
## 2.运行脚本  
默认参数threshold=5, period=3, path=./camera
```
python monitor.py --threshold=5 --period=3 --path=C:/Users/he/Desktop/camera
```
## 3.参数说明  
threshold:摄像头捕获到的画面变化量阈值，阈值越小越敏感  
period:摄像头捕获周期，单位秒  
path:捕获图片保存路径  

待改进：阈值动态实时调整
