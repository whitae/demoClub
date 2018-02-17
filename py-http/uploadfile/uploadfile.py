#-*-coding:utf-8-*-
#!usr/bin/python
# image.py
#-*-coding=utf-8-*-
from poster.encode import multipart_encode
import urllib2
import sys
from urllib2 import Request, urlopen, URLError, HTTPError
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
  
register_openers()
f=open("img.jpeg", "rb")
# headers 包含必须的 Content-Type 和 Content-Length
# datagen 是一个生成器对象，返回编码过后的参数
datagen, headers = multipart_encode({"data": f,"logo":"logo"})
# 创建请求对象
request = urllib2.Request("http://localhost:8000/data/upload", datagen, headers)
try:
    response = urllib2.urlopen(request)
    print response.read()
     
except URLError,e:
    print e.reason
