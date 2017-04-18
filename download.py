# coding=utf8
# 下载并保存视频流
import datetime
import win32api


# 中文转英文
def cn2en(txt):
    if txt == u'超清':
        return 'chaoqing'
    elif txt == u'高清':
        return 'gaoqing'
    elif txt == u'流畅':
        return 'liuchang'

# 调用ffmpeg.exe
# Qt_Infor 信息模块
# invedio: m3u8的地址
# tsUrl: ts地址的数组
# address: 星梦剧院地址
# id: 视频id
# pinzhi: 视频的质量
def download(Qt_Infor, m3u8, address, id, pinzhi, title):
    now = datetime.datetime.now()
    fl = address + '_' + id + '_' + cn2en(pinzhi) + '_' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.mp4' # 使用时间戳
    arg = '-i ' + m3u8 + ' -acodec copy -vcodec copy -f mp4 output/' + fl
    Qt_Infor.setText('下载视频：' + title + '\n' +
                     '输出文件：' + fl)
    win32api.ShellExecute(0, 'open', 'ffmpeg.exe', arg, '', True)