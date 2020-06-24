#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:43:32 2020

@author: linhaohong
"""

import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
for j in range(566,943):
    f=open('/Volumes/虚拟机/爬取文件/企业/{}.txt'.format(j),'a',encoding='utf-8')
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(j)
    data = requests.get(url=url,headers=headers).text
    S=re.compile('https://jobs.51job.com/all/(.*?).html',re.S).findall(data)
    for i in range(len(S)):
        S[i]='https://jobs.51job.com/all/{}.html'.format(S[i])
        req = requests.get(S[i],headers=headers)
        req.encoding='gbk'
        req=req.text
        compare=re.compile('<h1 title=(.*?)>',re.S).findall(req)
        com=''.join(compare)
        S1=re.compile('zw-name" title=".*?"(.*?)<span class="t5">',re.S).findall(req)
        for num in range(len(S1)):
            S1[num]=S1[num].replace('<span class="t2"','').replace('</a></p>','').replace('<span class="t3"','').replace('<span class="t4"','').replace('\n','').replace(' ','').replace('</span>','')
        f.write(com)
        for g in S1:
            f.write(g+'\n')
    print("完成{}页".format(j))
    f.close()