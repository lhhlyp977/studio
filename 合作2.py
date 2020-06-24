#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:16:41 2020

@author: linhaohong
"""
import requests
import re
import json
i=1
j_num=1
list=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
def json_com_n(nums,j_num):
    file_name='/Volumes/虚拟机/爬取文件/企业/jcompany_info_list{}.json'.format(j_num)
    with open(file_name, 'a',encoding='utf-8') as file_obj:
        json.dump(nums,file_obj,ensure_ascii=False)
for j in range(1,2):
    url = 'https://company.51job.com/p{}/'.format(j)
    data = requests.get(url=url,headers=headers).text
    S=re.compile('https://jobs.51job.com/all/co(.*?).html',re.S).findall(data)
    for j_j in range(len(S)):
        compare_all=[]
        for tt in range(1,3):
            url='https://msearch.51job.com/co_all_job.php?pageno={}&coid={}&jobarea=&funtype=&salary=&from='.format(i,S[j_j])
            i=i+1
            req = requests.get(url=url,headers=headers).text.encode("latin1").decode("utf-8") 
            compare_url=re.compile('"//msearch.51job.com/jobs/(.*?).html.*?rc=04"',re.S).findall(req)
            compare=re.compile('class="e"><h3>(.*?)</em>',re.S).findall(req)
            print(compare)
            for compare_url_number in range(len(compare_url)):
                compare_url[compare_url_number]=""+"//msearch.51job.com/jobs/{}.html?rc=04".format(compare_url[compare_url_number])
            for num in range(len(compare)):
                compare[num]=compare[num]+"|"+compare_url[num]
                compare[num]=compare[num].replace("<h3>"," ").replace("</h3><aside>"," ").replace("</aside><i>"," ").replace("</i><em>"," ").replace("|"," ")#招聘信息
                compare_temp=compare[num].split(' ')#变列
                compare[num]= [temp for temp in compare_temp if temp != '']
                """
                if compare[num]:
                    break
                else:
                    compare_all.append(compare[num])
                    print("成功")
        json_com_n(compare_all,j_num)
        print("great")
        j_num=j_num+1
        """
            
            
            
            