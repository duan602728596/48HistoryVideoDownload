# coding=utf8
# 警告框
from PyQt4 import QtGui

def warning(text):
    qtm = QtGui.QMessageBox
    msg = qtm(qtm.Warning, u'警告', text)
    msg.exec_()