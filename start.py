# coding=utf8
import sys
import os
from PyQt4 import uic, QtCore, QtGui
from getAddress import getAddress        # 请求地址
from addResultItem import addResultItem  # 地址添加到结果列表
from warning import warning              # 警告
from goToDownload import goToDownload    # 下载
import download                          # 停止下载

# ui地址
Ui_MainWindow, QtBaseClass = uic.loadUiType(os.getcwd() + '\\main.ui')


# 定义函数类
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
  def __init__(self):
    # Qt初始化
    QtGui.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    
    # 设置图标
    self.setWindowIcon(QtGui.QIcon(os.getcwd() + '\\icon2.ico'))
    
    # 参数
    self.page = 1           # 当前页数
    self.address = 'snh48'  # 地址
    self.pinzhi = u'超清'   # 视频品质
    self.list = []          # 当前列表
    
    # 链接函数
    self.initPage()
    self.Refresh_Btn.clicked.connect(self.refresh)    # 刷新按钮链接
    self.Back_Btn.clicked.connect(self.backPage)      # 上一页按钮链接
    self.Next_Btn.clicked.connect(self.nextPage)      # 上一页按钮链接
    self.Download_Btn.clicked.connect(self.download)  # 下载
    self.Stop_Btn.clicked.connect(self.stop)          # 停止下载
  
  # 初始化页数
  def initPage(self):
    self.Page_Label.setText(u'第' + str(self.page) + u'页')
  
  # 刷新
  def refresh(self):
    self.page = 1
    address = None
    try:
      address = self.Change_Address.currentItem().text(0)
    except:
      address = 'snh48'
    # 修改默认参数
    self.address = address
    self.list = getAddress(self.address, self.page)
    self.initPage()
    addResultItem(self.Result, self.list)
  
  # 上一页
  def backPage(self):
    if self.page != 1:
      self.page = self.page - 1
      self.list = getAddress(self.address, self.page)
      self.initPage()
      addResultItem(self.Result, self.list)
    else:
      warning(u'已经是第一页了')
  
  # 下一页
  def nextPage(self):
    self.list = getAddress(self.address, self.page + 1)
    
    if len(self.list) != 0:
      self.page = self.page + 1
      self.initPage()
      addResultItem(self.Result, self.list)
    else:
      warning(u'已经是最后一页了')
  
  # 下载
  def download(self):
    # 获取品质
    try:
      self.pinzhi = unicode(self.Pinzhi.currentItem().text(0))
    except:
      self.pinzhi = u'超清'
    
    # 获取要下载的项目
    try:
      title = unicode(self.Result.currentItem().text())
    except:
      title = None
      warning(u'请选择一个项目进行下载！')
    
    # 下载
    if title != None:
      download.stopDownload = False
      goToDownload(self.Infor, self.pinzhi, self.address, title)
  
  # 停止下载
  def stop(self):
    download.stopDownload = True


# 初始化程序
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = MyApp()
  window.show()
  sys.exit(app.exec_())
