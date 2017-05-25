# coding=utf8
# 进行get请求
import urllib


# get请求
# url: 请求的地址
def get(url):
  request = urllib.request.Request(url)
  response = urllib.request.urlopen(request)
  return response.read().decode()


# ts请求
# url：请求的地址
# headers：请求头
def getTs(url, headers):
  request = urllib.request.Request(url, headers=headers)
  r = None
  
  try:
    response = urllib.request.urlopen(request)
    r = response.read()
  except:
    r = 404
  
  return r
