#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:22:13 2020

@author: linhaohong
"""
def pp():
     s2=test.get()
     import urllib.request as r
     s1='http://api.openweathermap.org/data/2.5/weather?q='
     s3='&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
     url=s1+s2+s3
     data=r.urlopen(url).read().decode('utf-8')
     import json
     data=json.loads(data)
     l='温度:'+(str)(data['main']['temp'])+','+'天气:'+(str)(data['weather'][0]['description'])+','+'气压:'+(str)(data['main']['pressure'])
     tk.Label(root,textvariable=l)
     #l.pack()
import tkinter as tk
root = tk.Tk()
root.title('前端天气可视化')
test=tk.Entry(root)
B=tk.Button(root,text ="点我",command = pp())
B.pack()
test.pack()
root.mainloop()


