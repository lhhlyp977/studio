#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:52:46 2020

@author: linhaohong
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=huidong,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
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