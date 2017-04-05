# coding=utf8
# 请求地址
import urllib
import re
from pyquery import PyQuery

RE = re.compile(r'\d*', re.I)

# find
def find(reResult):
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


# 获取地址
def getAddress(address, page):
    # 获取数据
    try:
        url = 'http://live.' + address + '.com/Index/index/p/' + str(page) + '.html'
        request = urllib.request.Request(str(url))
        response = urllib.request.urlopen(request)
        read = response.read().decode()
    except:
        read = None

    # 判断是否有数据
    list = []

    if read != None:
        # 对数据进行查询并添加到列表里
        query = PyQuery(read)

        # 查询
        i = 0
        while True:
            video = query('.videos').eq(i)
            if video:
                html = PyQuery(video)
                obj = {
                    'title': html('h4').text() + ', ' + html('p').text(),
                    'id': find(RE.findall(html('a').attr('href'))),
                }
                list.append(obj)
                i += 1
            else:
                break
    # 返回
    return list

