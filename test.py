#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:33:34 2020

@author: linhaohong
"""

import urllib.request as r
s1='http://api.openweathermap.org/data/2.5/weather?q='
s2='&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
s3=input('输入地区名')
url=s1+s3+s2
data=r.urlopen(url).read().decode('utf-8')
import json
data=json.loads(data)
print(f"温度:{data['main']['temp']},天气:{data['weather'][0]['description']},气压:{data['main']['pressure']}")