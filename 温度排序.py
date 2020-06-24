#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:10:15 2020

@author: linhaohong
"""

import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
tem=[]
import json
data=json.loads(data)

print('='*73)
print('|        日期        |  温度  |  最高气温  |  最低气温  |  天气情况  |  气压  |')
print('-'*73)
print(f"|{data['list'][4]['dt_txt']} | {data['list'][4]['main']['temp']} |   {data['list'][4]['main']['temp_max']}   |   {data['list'][4]['main']['temp_min']}  |  {data['list'][4]['weather'][0]['description']}  |  {data['list'][4]['main']['pressure']} |")
print('-'*73)
print(f"|{data['list'][12]['dt_txt']} | {data['list'][12]['main']['temp']} |   {data['list'][12]['main']['temp_max']}   |   {data['list'][12]['main']['temp_min']}  |     {data['list'][12]['weather'][0]['description']}    |  {data['list'][12]['main']['pressure']} |")
print('-'*73)
print(f"|{data['list'][20]['dt_txt']} | {data['list'][20]['main']['temp']} |   {data['list'][20]['main']['temp_max']}   |   {data['list'][20]['main']['temp_min']}  |    {data['list'][20]['weather'][0]['description']}    |  {data['list'][20]['main']['pressure']} |")
print('-'*73)
print(f"|{data['list'][28]['dt_txt']} | {data['list'][28]['main']['temp']} |   {data['list'][28]['main']['temp_max']}   |   {data['list'][28]['main']['temp_min']}  |    {data['list'][28]['weather'][0]['description']}    |  {data['list'][28]['main']['pressure']} |")
print('-'*73)
print(f"|{data['list'][36]['dt_txt']} |   {data['list'][36]['main']['temp']}  |     {data['list'][36]['main']['temp_max']}    |    {data['list'][36]['main']['temp_min']}    |  {data['list'][36]['weather'][0]['description']}  |  {data['list'][36]['main']['pressure']} |")
print('='*73)
for i in range(4,37,8):
    tem.append(data['list'][i]['main']['temp'])
tem1=sorted(tem)
print("从小到大的温度排序是：")
for j in range(5):
    print(f"{tem1[j]} , ",end="")
print()
print(f"最大温度是{max(tem1)}")
print(f"最小温度是{min(tem1)}")
