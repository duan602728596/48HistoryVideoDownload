"""
功能：
官网录播公演下载
官网直播录源

python版本：v3
依赖外部工具：ffmpeg

依赖模块：
PyQt5
PyQuery
lxml
pyinstaller
"""
import sys
from PyQt5 import QtWidgets
from modules.MainWindow import MainWindow

# 初始化程序
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())