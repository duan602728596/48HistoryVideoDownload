"""
程序界面相关，绑定函数与响应

address: 录播地址
quality: 品质
videoList: 列表
page: 当前页
prev_btn: 上一页
next_btn: 下一页
download: 下载
refresh: 刷新
address_inLive: 直播地址
quality_inLive: 直播品质
recording: 开始录源
infor_inLive: 提示
"""

import threading
import re
from PyQt5 import uic, QtGui, QtWidgets
from modules.DownLoad import download
from modules.InLive import inLive
from modules.Message import message
from modules.config import LAYOUT, ICON

# 加载PyQt5的ui文件
Ui_MainWindow, QtBaseClass = uic.loadUiType(LAYOUT)

# 定义函数类
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    # Qt初始化
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    # 设置图标
    self.setWindowIcon(QtGui.QIcon(ICON))
    # 变量
    self.value_page = None
    # 绑定函数
    self.refresh.clicked.connect(self.onReFresh)
    self.prev_btn.clicked.connect(self.onPrevPage)
    self.next_btn.clicked.connect(self.onNextPage)
    self.download.clicked.connect(self.onDownLoad)
    self.recording.clicked.connect(self.onInLive)
  
  # 刷新回调函数
  def onReFreshCallBack(self, list):
    # 修改ui
    self.page.setText('第' + str(self.value_page) + '页')
    self.videoList.clear()
    i = 0
    length = len(list)
    while i < length:
      s = 'ID: ' + str(list[i]['id']) + ', ' + list[i]['title']
      self.videoList.addItem(s)
      i += 1

  def onReFreshCallBack2(self, list):
    if len(list) != 0:
      if self.value_page == None:
        self.value_page = 1
      else:
        self.value_page += 1
      self.onReFreshCallBack(list)
    else:
      self.page.setText('第' + str(self.value_page) + '页  已经是最后一页！')
    
  # 刷新
  def onReFresh(self):
    address = self.address.currentItem().text(0)
    self.value_page = 1
    thread = threading.Thread(target=download.getAddress, args=(address, self.value_page, self.onReFreshCallBack))
    thread.start()
    
  # 上一页
  def onPrevPage(self):
    if self.value_page == 1:
      self.page.setText('第' + str(self.value_page) + '页  已经是第一页！')
    else:
      address = None
      try:
        address = self.address.currentItem().text(0)
      except:
        address = 'SNH48'
      if self.value_page == None:
        self.value_page = 1
      else:
        self.value_page -= 1
      thread = threading.Thread(target=download.getAddress, args=(address, self.value_page, self.onReFreshCallBack))
      thread.start()
      
  # 下一页
  def onNextPage(self):
    address = self.address.currentItem().text(0)
    vp = None
    if self.value_page == None:
      vp = 1
    else:
      vp = self.value_page + 1
    thread = threading.Thread(target=download.getAddress, args=(address, vp, self.onReFreshCallBack2))
    thread.start()

  # 获取id
  def getId(self, title):
    RE = re.compile(r'\d*', re.I)
    s = RE.findall(title)
    r = None
    i = 0
    j = len(s)
    while i < j:
      if s[i] != '':
        r = s[i]
        break
      else:
        i += 1
    return r
    
  # 下载
  def onDownLoad(self):
    address = None
    quality = None
    title = None
    # 地址
    try:
      address = self.address.currentItem().text(0)
    except:
      address = 'SNH48'
    # 品质
    try:
      quality = self.quality.currentItem().text(0)
    except:
      quality = '超清'
    # 标题
    try:
      title = self.videoList.currentItem().text()
    except:
      message.warn('请选择一个项目进行下载！')
    # 下载
    if title != None:
      id = self.getId(title)
      thread = threading.Thread(target=download.downloadVideo, args=(address, quality, id))
      thread.start()
  
  # 直播录源
  def onInLive(self):
    address = None
    quality = None
    # 地址
    try:
      address = self.address_inLive.currentItem().text(0)
    except:
      message.warn('请选择一个地址！')
    # 品质
    try:
      quality = self.quality_inLive.currentItem().text(0)
    except:
      quality = '超清'
    if address != None:
      thread = threading.Thread(target=inLive.downloadVideo, args=(address, quality, self.infor_inLive))
      thread.start()