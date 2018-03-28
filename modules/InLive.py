"""
直播录源

地址：http://live.xxx.com/Index/inlive
"""
import time
import win32api
from modules.Live48 import Live48
from modules.config import FFMPEG, OUTPUT

class InLive(Live48):
  def __init__(self):
    super()
    # 直播地址
    self.URL = {
      'SNH48': 'http://zhibo.ckg48.com/',
      'BEJ48': 'http://live.bej48.com/',
      'GNZ48': 'http://live.gnz48.com/',
      'SHY48': 'http://live.shy48.com/',
      'CKG48': 'http://live.ckg48.com/',
    }
  
  # 录源
  def downloadVideo(self, address, quality, infor_inLive):  # 地址，品质，界面ui对象
    # 请求页面
    url = self.URL[address] + 'Index/inlive'
    result = self.get(url.lower())
    # 返回flv地址
    flv = self.getVideoValue(result, quality)
    if flv == None:
      infor_inLive.setText('公演未开始')
    else:
      title = '[直播]' + address + '_' + quality + '.' + time.strftime("%Y%m%d%H%M%S", time.localtime())
      outfile = OUTPUT + title + '.flv'
      arg = '-i "{flv}" -c copy "{output}"'.format(
        flv=flv,
        output=outfile,
      )
      win32api.ShellExecute(0, 'open', FFMPEG, arg, '', True)
      infor_inLive.setText('开始录源')
    
inLive = InLive()