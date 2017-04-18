# coding=utf8
# 进行get请求
import urllib2


# get请求
# url: 请求的地址
def get(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


# ts请求
# url：请求的地址
# headers：请求头
def getTs(url, headers):
    request = urllib2.Request(url, headers = headers)
    r = None

    try:
        response = urllib2.urlopen(request)
        r = response.read()
    except:
        r = 404

    return r