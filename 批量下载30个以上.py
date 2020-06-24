#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:09:03 2020

@author: linhaohong
"""
import pypinyin as pin
import urllib.request as r
import json

List1=['北京','上海','佛山','长春','沈阳','石家庄','合肥','福州','厦门','广州','深圳','济南','兰州','银川','太原','西安','郑州','南京','杭州','南昌','海口','南宁','贵阳','长沙','武汉','惠州','苏州','重庆','西宁','天津']
def pinyin(word):
    s = ''
    for i in pin.pinyin(word, style=pin.NORMAL):
        s += ''.join(i)
    return s

f=open('b.txt','a',encoding='utf-8')


for i in range(len(List1)):
    s3=(str)(pinyin(List1[i]))
    s1='http://api.openweathermap.org/data/2.5/weather?q='
    s2='&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    url=s1+s3+s2
    data=r.urlopen(url).read().decode('utf-8')
    data=json.loads(data)
    f.write(f"地区:{List1[i]},温度:{data['main']['temp']},天气:{data['weather'][0]['description']},气压:{data['main']['pressure']}\n")
f.close()