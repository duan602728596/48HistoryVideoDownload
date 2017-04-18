# coding=utf8
# 下载并保存视频流
import datetime
import re
from get import getTs


# 中文转英文
def cn2en(txt):
    if txt == u'超清':
        return 'chaoqing'
    elif txt == u'高清':
        return 'gaoqing'
    elif txt == u'流畅':
        return 'liuchang'


# 对地址进行解析
# invedio: m3u8地址
PATTERN_TSURL = re.compile(r'^http(s)?\:\/\/.+$', re.I)                     # 判断是否是以http(s)开头的地址
PATTERN_OLD = re.compile(r'http:\/\/ts\.snh48\.com\/\d+\/[a-z]+\/', re.I)   # 正则旧地址
PATTERN_NEW = re.compile(r'http:\/\/ts\.snh48\.com\/[^\d]+\/', re.I)        # 正则新地址
PATTERN_HOST = re.compile(r'http:\/\/ts\.snh48\.com.{0}', re.I)             # 正则新地址获取host

def getTsUrl(invedio, tsUrl):
    t = re.match(PATTERN_TSURL, tsUrl)
    r = ''

    if t == None:
        r = PATTERN_NEW.findall(invedio)
        if len(r) == 0:
            s = PATTERN_OLD.findall(invedio)
            r = s[0]
        else:
            s = PATTERN_HOST.findall(invedio)
            r = s[0]

    return r


# 下载所有的ts文件
# Qt_Infor 信息模块
# invedio: m3u8的地址
# tsUrl: ts地址的数组
# address: 星梦剧院地址
# id: 视频id
# pinzhi: 视频的质量
stopDownLoad = False # 用于停止下载

def download(Qt_Infor, invedio, getInvedio, tsUrl, address, id, pinzhi):
    # 文件io
    now = datetime.datetime.now()
    fl = address + '_' + id + '_' + cn2en(pinzhi) + '_' + now.strftime('%Y-%m-%d-%H-%M-%S') + '.ts' # 使用时间戳
    file = open('ts/' + fl, 'ab')

    # 获取ts的文件列表
    ts = getTsUrl(getInvedio, tsUrl[0])

    #请求头
    headers = {
        'Referer': invedio,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'ShockwaveFlash/24.0.0.221',
    }

    # 循环获取ts流
    i = 0
    length = len(tsUrl)
    while i < length:
        global stopDownLoad
        if stopDownLoad == False:
            # 二进制文件流
            u = ts + tsUrl[i] + '.ts'
            buffer = getTs(u, headers)

            # 状态码
            code = None
            if buffer != 404:
                file.write(buffer)
                code = '200'
            else:
                code = '404'

            # 更新进度条和信息
            Qt_Infor.setText(u'写入文件：' + fl + '\n' +
                            str(i + 1) + '/' + str(length) + ' ' + ts + tsUrl[i] + '.ts ' + code)
            i += 1

            # 判断是否完成
            if i == length:
                Qt_Infor.setText(u'下载成功：' + fl + '\n')
        else:
            Qt_Infor.setText(u'下载停止：' + fl + '\n')
            break
    file.close()