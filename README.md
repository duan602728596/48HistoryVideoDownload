# 48Live

## 功能
48G公演录播下载和直播录源

## 文件夹结构
* dependent: 依赖的文件存储目录
  * ffmpeg: ffmpeg
* output: 视频、Excel等文件的输出目录
* ui: 软件的图标和界面ui文件

## 依赖模块
> 需要python v3版本
* PyQt5
* PyQuery
* lxml
* pyinstaller用来打包编译

## 编译方法
1、运行`pyinstaller 48Live.py -w`   
2、将dependent、output、ui等文件夹拷贝到编译后的dist文件夹内

## 源代码地址
[https://github.com/duan602728596/48Live](https://github.com/duan602728596/48Live)