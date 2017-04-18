# coding=utf8
# 下载并保存视频流
import datetime
import re
import win32api
from get import getTs


# 中文转英文
def cn2en(txt):
    if txt == '超清':
        return 'chaoqing'
    elif txt == '高清':
        return 'gaoqing'
    elif txt == '流畅':
        return 'liuchang'


# 对地址进行解析
# invedio：m3u8地址
PATTERN_URL1 = re.compile(r'http://ts\.snh48\.com/\d+/', re.I) # 旧网址
PATTERN_URL2 = re.compile(r'http://ts\.snh48\.com/\d+/[^\.]+/', re.I)   # 提取网址
def getTsUrl(m3u8):
    s = None
    r1 = PATTERN_URL1.findall(m3u8)
    r2 = PATTERN_URL2.findall(m3u8)

    if len(r2) != 0:
        s = r2[0]
    elif len(r1) != 0:
        s = r1[0]
    else:
        pass

    return s

# 调用ffmpeg.exe
# Qt_Infor 信息模块
# invedio: m3u8的地址
# tsUrl: ts地址的数组
# address: 星梦剧院地址
# id: 视频id
# pinzhi: 视频的质量
stopDownload = False
def download(Qt_Infor, invedio, m3u8, tsUrl, address, id, pinzhi, title):
    now = datetime.datetime.now()
    host = getTsUrl(m3u8)
    fl = address + '_' + id + '_' + cn2en(pinzhi) + '_' + now.strftime('%Y-%m-%d-%H-%M-%S')  # 使用时间戳

    # 新的url使用ffmpeg进行下载
    if host == None:
        arg = '-i ' + m3u8 + ' -acodec copy -vcodec copy -f mp4 output/' + fl + '.mp4'
        Qt_Infor.setText('下载视频：' + title + '\n' +
                         '输出文件：' + fl + '.mp4')
        win32api.ShellExecute(0, 'open', 'ffmpeg.exe', arg, '', True)

    # 旧的url使用传统的get方法下载
    else:
        headers = {
            'Referer': invedio,
            'X-Requested-With': 'ShockwaveFlash/24.0.0.221',
        }
        file = open('output/' + fl + '.ts', 'ab')
        i = 0
        length = len(tsUrl)
        while i < length:
            global stopDownload
            if stopDownload == False:
                u = host + tsUrl[i] + '.ts'
                buffer = getTs(u, headers)

                code = None
                if buffer != 404:
                    file.write(buffer)
                    code = '200'
                else:
                    code = '404'

                Qt_Infor.setText('写入文件：' + fl + '.ts' + '\n' +
                                 str(i + 1) + '/' + str(length) + ' ' + host + tsUrl[i] + '.ts ' + code)
                i += 1

                if i == length:
                    Qt_Infor.setText('下载完成：' + fl + '.ts' + '\n' +
                                     str(i + 1) + '/' + str(length) + ' ' + host + tsUrl[i] + '.ts')
            else:
                Qt_Infor.setText('停止下载：' + fl + '.ts' + '\n' +
                                 str(i + 1) + '/' + str(length) + ' ' + host + tsUrl[i] + '.ts')
                break




