#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:30:24 2020

@author: linhaohong
"""

import requests
import re
import time
# http://mpic.tiankong.com/fff/a07/fffa07d7409dfcad0ca9f996f42a9112/640.jpg@!240h   图片网址
url = r'https://www.quanjing.com/creative/topic/1'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}
r = requests.get(url,headers = header)
# print(type(r.text))
pat=r'http://mpic.tiankong.com/(.*?)/640.jpg@!240h'#设置匹配正则表达式
re_im = re.compile(pat,re.S)
imList = re_im.findall(r.text)#获取符合要求的字符串列表
print(r.text)
print("开始下载了...")
for i in range(len(imList)):
    src = 'http://mpic.tiankong.com/' + imList[i] + '/640.jpg@!240h'
    url = "/Users/linhaohong/Desktop/图片/" + str(i+1) + ".jpg"
    r = requests.get(src)
    with open(url, 'wb') as f:#下载图片
        f.write(r.content)
    time.sleep(0.1)#下载间隔时间
    print("下载完%d张了..."%(i+1))