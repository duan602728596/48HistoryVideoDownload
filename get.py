# coding=utf8
# 进行get请求
import urllib2


# get请求
# url: 请求的地址
def get(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()