# coding=utf8
# 下载前的处理
import re
import threading
from pyquery import PyQuery
from download import download
from get import get


# 获取id
def getId(id):
    RE = re.compile(r'\d*', re.I)
    s = RE.findall(id)
    r = None

    i = 0
    j = len(s)
    while i < j:
        if s[i] != u'':
            r = s[i]
            break
        else:
            i += 1

    return r


# ----------------------------------------------------------------------
# 获取高清或者超清地址
# 获取高清地址
# txt: 获取的html字符串
def gaoQingUrl(txt):
    page = PyQuery(txt)
    return page('#gao_url').attr('value')


# 获取超清地址
# txt: 获取的html字符串
def chaoQingUrl(txt):
    page = PyQuery(txt)
    return page('#chao_url').attr('value')


# 获取流畅地址
# txt: 获取的html字符串
def liuChangUrl(txt):
    page = PyQuery(txt)
    return page('#liuchang_url').attr('value')


# ----------------------------------------------------------------------
# 根据品质返回地址
# num: 参数
# txt: 获取的html字符串
def pinZhi(pinzhi, txt):
    pz = pinzhi
    # 超清
    if pz == u'超清':
        return chaoQingUrl(txt)
    # 高清
    elif pz == u'高清':
        return gaoQingUrl(txt)
    # 流畅
    elif pz == u'流畅':
        return liuChangUrl(txt)


# ----------------------------------------------------------------------
# 对m3u8进行处理，获取所有的ts地址
PATTERN_TS = re.compile(r'\n([^\#\,\n]*)\.ts', re.I)
def ts(m3u8Html):
    # 正则匹配.ts地址
    r = PATTERN_TS.findall(m3u8Html)
    return r


# ----------------------------------------------------------------------
# 下载
def goToDownload(Qt_Infor, pinzhi, address, title):
    id = getId(title)
    # 获取页面
    invedio = str('http://live.' + address + '.com/Index/invedio/id/' + id)
    getInvedio = get(invedio)

    # 根据页面获取m3u8文件
    m3u8 = pinZhi(pinzhi, getInvedio)
    m3u8Html = get(m3u8)

    # 返回ts的地址
    tsUrl = ts(m3u8Html)

    # 创建新线程下载
    thread1 = threading.Thread(target = download, args = (Qt_Infor, invedio, m3u8, tsUrl, address, id, pinzhi, title))
    thread1.start()