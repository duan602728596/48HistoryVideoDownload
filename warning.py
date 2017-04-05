# coding=utf8
# 警告框
from PyQt5 import QtWidgets

def warning(text):
    qtm = QtWidgets.QMessageBox
    msg = qtm(qtm.Warning, u'警告', text)
    msg.exec_()