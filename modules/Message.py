"""
提示框类

warn: 警告
"""
from PyQt5 import QtWidgets

class Message:
  def __init__(self):
    self.messageBox = QtWidgets.QMessageBox
  
  # 警告框
  def warn(self, text):
    msg = self.messageBox(self.messageBox.Warning, u'警告', text)
    msg.exec_()
    
message = Message()