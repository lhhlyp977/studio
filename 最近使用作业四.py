#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:05:23 2020

@author: linhaohong
"""
import json
import requests
import re

file_name='/Volumes/虚拟机/爬取文件/企业1/company_list1(1).json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
def json_com_n(nums,j_num):
    file_name='/Volumes/虚拟机/爬取文件/企业1/company_info_list[{}].json'.format(j_num)
    with open(file_name, 'w',encoding='utf-8') as file_obj:
        json.dump(nums,file_obj,ensure_ascii=False)
"""
def error_list(nums,j_num):
    file_name='/Volumes/虚拟机/爬取文件/企业1/error_list[{}].json'.format(j_num)
    with open(file_name, 'w',encoding='utf-8') as file_obj:
        json.dump(nums,file_obj,ensure_ascii=False)
"""
with open(file_name, 'r',encoding='utf-8') as file_obj:
    task = json.loads(file_obj.read())
#print(task)
company_info_list=[]
error_list=[]
for i in task:
    compare_news=['','','']
    company_info_list_temp=['']
    url =i[5]
    #try:
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
    #print(compare_news[0])
    compare_news[0]=[a[0]]
    compare_news[1]=[a2_str.replace(" ","")]
    compare_news[2]=[a3_str.replace(" ","")]
    i.append(compare_news)
    company_info_list.append(i)
    print(company_info_list)
"""
    company_info_list_temp[0]=i
    company_info_list_temp[1]=compare_news
    company_info_list.append(company_info_list_temp)
    print("成功一个")
    except:
        error_list_temp=[]
        error_list.append()
"""
json_com_n(company_info_list,1)
