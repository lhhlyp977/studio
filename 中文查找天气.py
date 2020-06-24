#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:08:16 2020

@author: linhaohong
"""
import pypinyin as pin

import urllib.request as r
def pinyin(word):
    s = ''
    for i in pin.pinyin(word, style=pin.NORMAL):
        s += ''.join(i)
        return s
s2=''
S=input('输入城市（中文）')
for i in range(len(S)):
    s2+=pinyin(S[i])

s1='http://api.openweathermap.org/data/2.5/forecast?q='
s3=',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
url=s1+s2+s3
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
    
print(f"今天是:{data['list'][4]['dt_txt']}，温度是:{data['list'][4]['main']['temp']}，最高气温:{data['list'][4]['main']['temp_max']}，最低气温:{data['list'][4]['main']['temp_min']}，天气情况是:{data['list'][4]['weather'][0]['description']}，气压是:{data['list'][4]['main']['pressure']}")
print(f"今天是:{data['list'][12]['dt_txt']}，温度是:{data['list'][12]['main']['temp']}，最高气温:{data['list'][12]['main']['temp_max']}，最低气温:{data['list'][12]['main']['temp_min']}，天气情况是:{data['list'][12]['weather'][0]['description']}，气压是:{data['list'][12]['main']['pressure']}")
print(f"今天是:{data['list'][20]['dt_txt']}，温度是:{data['list'][20]['main']['temp']}，最高气温:{data['list'][20]['main']['temp_max']}，最低气温:{data['list'][20]['main']['temp_min']}，天气情况是:{data['list'][20]['weather'][0]['description']}，气压是:{data['list'][20]['main']['pressure']}")
print(f"今天是:{data['list'][28]['dt_txt']}，温度是:{data['list'][28]['main']['temp']}，最高气温:{data['list'][28]['main']['temp_max']}，最低气温:{data['list'][28]['main']['temp_min']}，天气情况是:{data['list'][28]['weather'][0]['description']}，气压是:{data['list'][28]['main']['pressure']}")
print(f"今天是:{data['list'][36]['dt_txt']}，温度是:{data['list'][36]['main']['temp']}，最高气温:{data['list'][36]['main']['temp_max']}，最低气温:{data['list'][36]['main']['temp_min']}，天气情况是:{data['list'][36]['weather'][0]['description']}，气压是:{data['list'][36]['main']['pressure']}")
print(f"{data['list'][4]['dt_txt']},温度{(int)(data['list'][4]['main']['temp'])*'-'}{data['list'][4]['main']['temp']}")
print(f"{data['list'][12]['dt_txt']},温度{(int)(data['list'][12]['main']['temp'])*'-'}{data['list'][12]['main']['temp']}")
print(f"{data['list'][20]['dt_txt']},温度{(int)(data['list'][20]['main']['temp'])*'-'}{data['list'][20]['main']['temp']}")
print(f"{data['list'][28]['dt_txt']},温度{(int)(data['list'][28]['main']['temp'])*'-'}{data['list'][28]['main']['temp']}")
print(f"{data['list'][36]['dt_txt']},温度{(int)(data['list'][36]['main']['temp'])*'-'}{data['list'][36]['main']['temp']}")