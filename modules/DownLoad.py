"""
下载录播

将m3u8文件下载到本地，并且对url进行格式化
启动shell进行下载，下载时会出现命令行
"""
import re
import time
import win32api
import urllib.parse
from pyquery import PyQuery
from modules.Live48 import Live48
from modules.config import FFMPEG, OUTPUT

class DownLoad(Live48):
  def __init__(self):
    super()
    self.ID = re.compile(r'\d*', re.I)                        # 匹配id
    self.TS_URL = re.compile(r'(?<=\n)[^#\n]*(?=\n)', re.I)   # 匹配m3u8内的ts地址
    self.IS_HTTP = re.compile(r'^ht{2}ps?', re.I)             # 是否是http或https
    self.IS_SLASH = re.compile(r'^\/.+$', re.I)               # 是否以斜杠开头
    self.M3U8_FILE_NAME = re.compile(r'[^/]+\.m3u8.*')        # 提取文件名
  
  # 获取地址中的id
  def find(self, reResult):
    i = 0
    j = len(reResult)
    r = None
    while i < j:
      if reResult[i] != '':
        r = reResult[i]
        break
      else:
        i += 1
    return r
  
  # 下载地址列表
  def getAddress(self, address, value_page, callback):
    # 请求数据
    pageStr = str(value_page)
    url = 'http://live.' + address + '.com/Index/index/p/' + pageStr + '.html'
    read = self.get(url)

    # 对数据进行查询并添加到列表里
    list = []
    query = PyQuery(read)
    i = 0
    while True:
      video = query('.videos').eq(i)
      if video:
        html = PyQuery(video)
        obj = {
          'title': html('h4').text() + ', ' + html('p').text(),
          'id': self.find(self.ID.findall(html('a').attr('href'))),
        }
        list.append(obj)
        i += 1
      else:
        break
        
    # 回调函数
    callback(list)
  
  # 下载
  def downloadVideo(self, address, quality, id): # 地址，品质，id
    # 请求页面
    url = 'http://live.' + address + '.com/Index/invedio/id/' + id
    result = self.get(url.lower())
    # 返回m3u8地址
    m3u8 = self.getVideoValue(result, quality)
    m3u8text = self.get(m3u8)
    # 使用正则解析网址
    tsUrl = self.TS_URL.findall(m3u8text)
    host = None
    if self.IS_HTTP.match(tsUrl[0]) != None:
      host = ''
    elif self.IS_SLASH.match(tsUrl[0]) != None:
      p = urllib.parse.urlparse(m3u8)
      host = p.scheme + '://' + p.netloc
    else:
      host = re.sub(self.M3U8_FILE_NAME, '', m3u8)
      pass
    # 使用正则替换网址
    i = 0
    j = len(tsUrl)
    while i < j:
      m3u8text = m3u8text.replace(tsUrl[i], host + tsUrl[i])
      i += 1
    # 写文件
    title = '[录播]' + address + '_' + id + '_' + quality + '.' + time.strftime("%Y%m%d%H%M%S", time.localtime())
    m3u8file = OUTPUT + title + '.m3u8'
    outfile = OUTPUT + title + '.mp4'
    file = open(m3u8file, 'w+')
    file.write(m3u8text)
    file.close()
    # 开启命令行下载
    arg = '-protocol_whitelist file,http,https,tcp,tls -i "{m3u8}" -acodec copy -vcodec copy -f mp4 "{output}"'.format(
      m3u8=m3u8file,
      output=outfile,
    )
    win32api.ShellExecute(0, 'open', FFMPEG, arg, '', True)
    
download = DownLoad()