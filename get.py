# coding=utf8
# 进行get请求
import urllib
import warning


# get请求
# url: 请求的地址
def get(url):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode()
    except:
        warning(u'请稍后下载')
