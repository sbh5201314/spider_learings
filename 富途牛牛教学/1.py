import execjs
with open('1.js', encoding='utf-8')as f:
    js_code = f.read()
_cell = execjs.compile(js_code)
import requests


headers = {
    "authority": "www.futunn.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "futu-x-csrf-token": "cd1zage106rT3rMaO8V7P4Cx",
    "pragma": "no-cache",
    "quote-token": "9190dae0c4",
    "referer": "https://www.futunn.com/quote/us?global_content=%7B%22promote_id%22%3A13766,%22sub_promote_id%22%3A24%7D&security_id=80298708786233",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
cookies = {
    "cipher_device_id": "1719910640764338",
    "_gcl_au": "1.1.1906948739.1719910646",
    "_fbp": "fb.1.1719910647009.942643682538399068",
    "_clck": "pd38ke%7C2%7Cfn4%7C0%7C1644",
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%22ftv1wKqA2Ptw6eoQLyLSVGYJjjrZfw6hfVpERCGgke%2BLgZwFY1Q82KrkzvDmBbSeQBEK%22%2C%22first_id%22%3A%2219072ab67511c-068d2b3183afef4-26001951-921600-19072ab6752ddd%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJmdHYxd0txQTJQdHc2ZW9RTHlMU1ZHWUpqanJaZnc2aGZWcEVSQ0dna2UrTGdad0ZZMVE4Mktya3p2RG1CYlNlUUJFSyIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxOTA3MmFiNjc1MTFjLTA2OGQyYjMxODNhZmVmNC0yNjAwMTk1MS05MjE2MDAtMTkwNzJhYjY3NTJkZGQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22ftv1wKqA2Ptw6eoQLyLSVGYJjjrZfw6hfVpERCGgke%2BLgZwFY1Q82KrkzvDmBbSeQBEK%22%7D%2C%22%24device_id%22%3A%2219072ab67511c-068d2b3183afef4-26001951-921600-19072ab6752ddd%22%7D",
    "_ga_K1RSSMGBHL": "GS1.1.1719930077.4.1.1719932031.0.0.0",
    "_ga_NTZDYESDX1": "GS1.2.1719930077.4.1.1719932031.22.0.0",
    "_uetvid": "1b162560385111ef88f69174ed519689",
    "device_id": "1719910640764338",
    "_gid": "GA1.2.1063664532.1722702663",
    "csrfToken": "cd1zage106rT3rMaO8V7P4Cx",
    "locale": "zh-cn",
    "locale.sig": "ObiqV0BmZw7fEycdGJRoK-Q0Yeuop294gBeiHL1LqgQ",
    "Hm_lvt_f3ecfeb354419b501942b6f9caf8d0db": "1722751358,1722758477,1722806448,1722815422",
    "Hm_lpvt_f3ecfeb354419b501942b6f9caf8d0db": "1722815422",
    "HMACCOUNT": "5BBA3AC815218848",
    "futunn_lang": "zh-CN",
    "passport_dp_data": "T0WjStSfPAWBfjyNnr8%2BP0zBS5t3JJcd73a8Ip2XLTpoZOITJ5FDp07diWXQ4T91ShTdHVrVWOSDVObMzfnXh8Ua9T0wd5h4h4zG2m1uNJ8%3D",
    "ftreport-jssdk%40session": "{%22distinctId%22:%22ftv1wKqA2Ptw6eoQLyLSVGYJjp9/2vlEnxcWaFs8m6S+1pMFY1Q82KrkzvDmBbSeQBEK%22%2C%22firstId%22:%22ftv1wKqA2Ptw6eoQLyLSVGYJjt/HVVuku0nxTQwek/C46eAFY1Q82KrkzvDmBbSeQBEK%22%2C%22latestReferrer%22:%22https://www.futunn.com/%22}",
    "_ga": "GA1.1.660232156.1719910642",
    "_ga_370Q8HQYD7": "GS1.1.1722815422.9.1.1722815425.57.0.0",
    "_ga_FZ1PVH4G8R": "GS1.1.1722815425.9.0.1722815425.0.0.0",
    "_ga_XECT8CPR37": "GS1.1.1722815422.10.1.1722815432.50.0.0",
    "_ga_EJJJZFNPTW": "GS1.1.1722815422.9.1.1722815442.0.0.0"
}
url = "https://www.futunn.com/quote-api/quote-v2/get-stock-list"
def get_data(page):

    params = {
        "marketType": "2",
        "plateType": "1",
        "rankType": "1",
        "page": page,
        "pageSize": "50"
    }
    headers['quote-token'] = _cell.call('get_token', params)
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    itme_list = response.json()['data']['list']

    for i in itme_list:
        b = {"股票名称": i['name'], "股票代码": i['stockCode'], "涨跌额": i['change'], "涨跌幅": i['changeRatio']}
        print(b)
        # a.append(b)
    print(f'第{page}爬取完成')
if __name__ == '__main__':
    for page in range(11):
        get_data(page)

