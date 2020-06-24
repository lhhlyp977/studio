#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 05:19:54 2020

@author: linhaohong
"""

import requests
import re
import json

j_num=1
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
def json_com_n(nums,j_num):
    file_name='/Volumes/虚拟机/爬取文件/企业1/company_info_list[{}].json'.format(j_num)
    with open(file_name, 'a',encoding='utf-8') as file_obj:
        json.dump(nums,file_obj,ensure_ascii=False)
for j in range(1,5):
    a3_str=""
    a2_str=""
    url = 'https://company.51job.com/p{}/'.format(j)
    data = requests.get(url=url,headers=headers).text
    S=re.compile('https://jobs.51job.com/all/co(.*?).html',re.S).findall(data)
    for j_j in range(len(S)):
        compare_news=['','','','']
        url = 'https://jobs.51job.com/all/co{}.html'.format(S[j_j])
        data = requests.get(url=url,headers=headers)
        data.encoding='gbk'
        data=data.text
        a=re.compile('class="con_txt">(.*?)</div>',re.S).findall(data)
        a[0]=a[0].replace("<br>"," ").replace("&nbsp;","")#公司简介
        a1=re.compile('<h1 title=(.*?)>',re.S).findall(data)#公司名称
        a2=re.compile('<p class="fp">.*?<span class="label">.*?</span>(.*?)</p>',re.S).findall(data)#公司地址
        a3=re.compile('<p class="fp tmsg"><span class="label">.*?</span><span>(.*?)</span>',re.S).findall(data)#公司官网网址
        a2_str="".join(a2)
        a3_str="".join(a3)
        compare_news[0]=a1[0]
        print(compare_news[0])
        compare_news[1]=a[0]
        compare_news[2]=a2_str.replace(" ","")
        compare_news[3]=a3_str.replace(" ","")
        json_com_n(compare_news,j_num)
        j_num=j_num+1
        print("成功")
       























































