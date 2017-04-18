# coding=utf8
# 进行get请求
import urllib


# get请求
# url: 请求的地址
def get(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read().decode()
