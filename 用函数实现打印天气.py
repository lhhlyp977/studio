#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:09:48 2020

@author: linhaohong
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=\
zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
def print_weather(i):
    print(f"今天是:{data['list'][i]['dt_txt']}，\
温度是:{data['list'][i]['main']['temp']}，\
最高气温:{data['list'][i]['main']['temp_max']}，\
最低气温:{data['list'][i]['main']['temp_min']}，\
天气情况是:{data['list'][i]['weather'][0]['description']}，\
气压是:{data['list'][i]['main']['pressure']}")
def print_list(i):
    print(f"{data['list'][i]['dt_txt']},\
温度{(int)(data['list'][i]['main']['temp'])*'*'}\
{data['list'][i]['main']['temp']}")
for i in range(0,40):
    print_weather(i)
for i in range(0,40):
    print_list(i)