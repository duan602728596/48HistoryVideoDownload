"""
下载直播或者录播

DownLoad和InLive都继承自该类
"""
import urllib.request
from pyquery import PyQuery

class Live48:
  def __init__(self):
    pass

  # 解析视频地址
  def getVideoValue(self, html, quality):
    page = PyQuery(html)
    # 超清
    if quality == '超清':
      return page('#chao_url').attr('value')
    # 高清
    elif quality == '高清':
      return page('#gao_url').attr('value')
    # 流畅
    elif quality == '流畅':
      return page('#liuchang_url').attr('value')

  # get请求
  def get(self, url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read().decode()