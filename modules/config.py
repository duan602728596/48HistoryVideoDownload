"""
配置文件
"""
import os

CWD = os.getcwd()

# 引用的图标，ui位置
LAYOUT =  CWD + '\\ui\\window.ui'
ICON = CWD + '\\ui\\icon.ico'

# ffmpeg.exe文件地址
FFMPEG = CWD + '\\dependent\\ffmpeg\\ffmpeg.exe'

# 文件输出目录
OUTPUT = CWD + '\\output\\'