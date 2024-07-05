#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 测试.py
# @Author:  抱枕红河谷
# @Date  : 2024/3/12 20:39
# @Desc  :
# @Contact :
import requests
session = requests.session()
import re
import json
import execjs
import requests
import time



headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Origin": "https://we.51job.com",
    "Pragma": "no-cache",
    "Referer": "https://we.51job.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
proxy = {
            'http1': 'http://114.231.45.11:8888',
            'http2': 'http://113.121.38.12:9999',
            'http3': 'http://114.231.42.231:8888',
            'http4': 'http://180.121.129.132:8888',
            'http5': 'http://60.170.204.30:8060',
        }

def get_one(job, page):
    cookies = {
    }
    url = "https://oauth.51job.com/ajax/get_token.php"
    params = {
        "fromdomain": "51job_web"
    }
    # response = session.post(url, headers=headers, cookies=cookies, params=params)
    # guid = response.cookies.get('guid')
    # cookies.update({"guid": guid})
    url2 = "https://we.51job.com/api/job/search-pc"
    params2 = {
        "api_key": "51job",
        "timestamp":str(int(time.time())),
        "keyword": job,
        "searchType": "2",
        "function": "",
        "industry": "",
        "jobArea": "000000",
        "jobArea2": "",
        "landmark": "",
        "metro": "",
        "salary": "",
        "workYear": "",
        "degree": "",
        "companyType": "",
        "companySize": "",
        "jobType": "",
        "issueDate": "",
        "sortType": "0",
        "pageNum": page,
        "requestId": "",
        "pageSize": "20",
        "source": "1",
        "accountId": "",
        "pageCode": "sou|sou|soulb"
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "User-Token": "",
        "Uuid": "17102471139993205879",
        "From-Domain": "51job_web",
        "Pragma": "no-cache",
        "Referer": "https://we.51job.com/pc/search?keyword=&searchType=2&sortType=0&metro=",
    }
    response_two = session.get(url2, params=params2,headers=headers2,cookies=cookies,)
    arg1 = re.findall("var arg1='(.*?)';",response_two.text)[0]
    # print(response_two.text)
    with open("51job_list_decrypt.js", "r", encoding='UTF-8') as file:
        js_code = file.read()
    list_decrypt_context = execjs.compile(js_code)
    acw_sc__v2 = list_decrypt_context.call("get_acw_sc__v2", arg1)
    cookies.update({'acw_sc__v2': acw_sc__v2})
    response_three = session.get(url2, cookies=cookies, headers=headers2,params=params2,)
    job_list = response_three.json()['resultbody']['job']['items']
    for i in job_list:
        a = {}
        jobname = i['jobName']
        salary = i['provideSalaryString']
        fullCompanyName = i['fullCompanyName']
        a['岗位'] = jobname
        a['薪水'] = salary
        a['公司名称'] = fullCompanyName
        print(a)


if __name__ == '__main__':
    job = input("请输入你要查询的职位")

    for i in range(1, 5):
        get_one(job, i)




 
