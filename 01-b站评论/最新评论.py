#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 最新评论.py
# @Author:  抱枕红河谷
# @Date  : 2023/11/29 10:45
# @Desc  :
# @Contact : 2082342522@qq.com


"""

需要安装的第三方库
pip install requests -i https://pypi.douban.com/simple
requests
xlwt
PyExecJS

视频讲解链接 ： https://www.bilibili.com/video/BV1fc411b7iq/?spm_id_from=333.999.0.0&vd_source=affe1de7053301ac364a3976db91efed
cookie有时效性 过期拿自己的cookie
"""
import execjs
import random
import requests
import time
import xlwt
# 创建一个workbook对象
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet对象
worksheet = workbook.add_sheet('Sheet1')
# worksheet.write(0, 0, 'Hello')
# worksheet.write(0, 1, 'World')
worksheet.write(0, 0, '用户昵称')
worksheet.write(0, 2, '内容')
worksheet.write(0, 1, '发布时间')
temp = 0


aa = "buvid3=147DB5B6-8168-3ABA-9FDD-380351F2095B41270infoc; b_nut=1691286241; i-wanna-go-back=-1; b_ut=7; _uuid=571FFB54-316A-1A410-810ED-1CD38FF4831C41170infoc; buvid4=5DF7E3F1-6263-8FDC-E340-1DD75E623AB243209-023080609-IP70lVFDMZe6UvqoRugC2w%3D%3D; rpdid=|(k)~uu)mkR~0J'uYmuk)YJkm; buvid_fp_plain=undefined; LIVE_BUVID=AUTO9716927917237525; hit-new-style-dyn=1; hit-dyn-v2=1; is-2022-channel=1; enable_web_push=DISABLE; header_theme_version=CLOSE; CURRENT_FNVAL=4048; DedeUserID=3546614742387091; DedeUserID__ckMd5=f47fd39ec30a7d48; CURRENT_QUALITY=80; FEED_LIVE_VERSION=V_DYN_LIVING_UP; fingerprint=6008ecc2173428d1835903b730b20089; home_feed_column=4; buvid_fp=6008ecc2173428d1835903b730b20089; browser_resolution=1280-559; PVID=2; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY4MzQ3MDEsImlhdCI6MTcxNjU3NTQ0MSwicGx0IjotMX0.uHwgSUvhkDZcbwe3yMxi_QjcXjdxehjvYlYz7wjepJM; bili_ticket_expires=1716834641; SESSDATA=131c1aea%2C1732127503%2Cb6442%2A52CjAS5hBY7ScozGFpdNm3RnuL1F4AylrubF4rEs11Bf2lL1aJ72WBEVuc1u-VvCiEeukSVlZqT2lwZXFKR3VUdmdpdWNuUk9DMXJSSDZvV3JiUjJGV1pXNl8xN1FPaE1GTERBWjF5bG44ZVFyeUQ5QUNlNThIS3N6Y0JGcjgtSEZkZHpEN1dwekFRIIEC; bili_jct=1f0d36f645db225fe5072a3d68b15902; sid=8th7s0oo; bp_t_offset_3546614742387091=936097777262264329; b_lsid=9CAEAB3B_18FB96185A3"

headers = {
    # "authority": "api.bilibili.com",
    # "accept": "*/*",
    # "accept-language": "zh-CN,zh;q=0.9",
    # "cache-control": "no-cache",
    # "origin": "https://www.bilibili.com",
    # "pragma": "no-cache",
    "cookies":aa,
    "referer": "https://www.bilibili.com/",
    # "sec-ch-ua": "^\\^Chromium^^;v=^\\^118^^, ^\\^Google",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "^\\^Windows^^",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
# cookie有时效性 未登录用户只能看前面三条评论
# cookie失效 使用自己的cookie
cookies_test = {
    "buvid3": "147DB5B6-8168-3ABA-9FDD-380351F2095B41270infoc",
    "b_nut": "1691286241",
    "i-wanna-go-back": "-1",
    "b_ut": "7",
    "_uuid": "571FFB54-316A-1A410-810ED-1CD38FF4831C41170infoc",
    "FEED_LIVE_VERSION": "V8",
    "buvid4": "5DF7E3F1-6263-8FDC-E340-1DD75E623AB243209-023080609-IP70lVFDMZe6UvqoRugC2w%3D%3D",
    "SESSDATA": "7665423a%2C1706838300%2C208fd%2A82xrX5gzmAI9SWyMHXHydjbY_SGsusuW0eVgqh3D1Z2kt8qQp6iHHTDHMWdVCEwlpDATP4oQAAUgA",
    "bili_jct": "85edd3bc092f0cc6821f5380a8a777a6",
    "DedeUserID": "502371982",
    "DedeUserID__ckMd5": "62e9b53bd4edb8fc",
    "sid": "7wmn4l7i",
    "rpdid": "|(k)~uu)mkR~0J'uYmuk)YJkm",
    "CURRENT_QUALITY": "80",
    "header_theme_version": "CLOSE",
    "buvid_fp_plain": "undefined",
    "LIVE_BUVID": "AUTO9716927917237525",
    "hit-new-style-dyn": "1",
    "hit-dyn-v2": "1",
    "home_feed_column": "5",
    "browser_resolution": "1536-715",
    "bp_article_offset_502371982": "848973317709758504",
    "CURRENT_FNVAL": "4048",
    "enable_web_push": "DISABLE",
    "bp_video_offset_502371982": "855297897562898438",
    "fingerprint": "3f267624af75a32521df80e581cb332b",
    "buvid_fp": "ed11c1360ef0cb61ac2e8fe2f8bc3a08",
    "b_lsid": "B210BDF86_18B5B9B133D",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTgzMDgxNzksImlhdCI6MTY5ODA0ODkxOSwicGx0IjotMX0.NvmQARjrewXqK8vDFKKTIyogNCI80TsTsrUcr9p9ll8",
    "bili_ticket_expires": "1698308119",
    "PVID": "3"
}
url = "https://api.bilibili.com/x/v2/reply/wbi/main"
with open('demo.js', encoding='utf-8')as f:
    js_code = f.read()
_cell = execjs.compile(js_code)



def get_one():
    global temp
    params = {
        "oid": "408876644",
        "type": "1",
        "mode": "2",
        "pagination_str": "{\"offset\":\"\"}",
        "plat": "1",
        "seek_rpid": "",
        "web_location": "1315875",
    }

    json_data = _cell.call('get_data', params)
    params['w_rid'] = json_data['w_rid']
    params['wts'] = json_data['wts']
    res = requests.get(url, headers=headers, params=params)
    next = res.json()['data']['cursor']['next']
    content_list = res.json()['data']['replies']

    for i in content_list:
        temp += 1
        b = {}
        b['用户昵称'] = i['member']['uname']
        b['发布时间'] = i['reply_control']['time_desc']
        b['内容'] = i['content']['message']
        worksheet.write(temp, 0, b['用户昵称'])
        worksheet.write(temp, 1, b['发布时间'])
        worksheet.write(temp, 2, b['内容'])
        print(b)
    return next


def get_content(Next):
    global temp
    params = {
        "oid": "408876644",
        "type": "1",
        "mode": "2",
        "pagination_str": "{\"offset\":\"{\\\"type\\\":3,\\\"direction\\\":1,\\\"Data\\\":{\\\"cursor\\\":%s}}\"}" % Next,
        "plat": "1",
        # "seek_rpid": "",
        "web_location": "1315875",

    }


    json_data = _cell.call('get_data', params)
    params['w_rid'] = json_data['w_rid']
    params['wts'] = json_data['wts']
    res = requests.get(url, headers=headers, params=params)
    print("第二次请求返回的数据",res.text)
    next = res.json()['data']['cursor']['next']
    content_list = res.json()['data']['replies']

    for i in content_list:
        temp += 1
        b = {}
        b['用户昵称'] = i['member']['uname']
        # 抓包响应有 Python请求返回的响应没有
        # b['ip属地'] = i['reply_control']['location']
        b['发布时间'] = i['reply_control']['time_desc']
        b['内容'] = i['content']['message']
        replies = i['replies']
        if replies:
            for i in replies:
                reply = i['content']['message']
                print('二级评论', reply)

        # worksheet.write(temp, 0, b['用户昵称'])
        # worksheet.write(temp, 1, b['发布时间'])
        # worksheet.write(temp, 2, b['内容'])
        print(b)

        #  随机休眠2到5秒
    time.sleep(random.randint(2, 5))
    if next:
        get_content(next)

if __name__ == '__main__':
    a = get_one()
    print(a)
    b = get_content(a)
    workbook.save('马老师最新评论3.xls')







 
