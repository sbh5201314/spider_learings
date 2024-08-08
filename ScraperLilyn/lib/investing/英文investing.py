import json

import time

import requests
from lxml import etree
import threading
from queue import Queue

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.investing.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.investing.com/economic-calendar/",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "adBlockerNewUserDomains": "1721025192",
    "udid": "895c36723c47b68fbda0436d7a7c1451",
    "_gid": "GA1.2.836258884.1721025196",
    "im_sharedid": "729b4514-2c9e-4f49-a2de-c676382d0aed",
    "im_sharedid_cst": "3yxgLFoszg%3D%3D",
    "__eventn_id": "895c36723c47b68fbda0436d7a7c1451",
    "_fbp": "fb.1.1721028010993.384953089413032256",
    "hide_promo_strip": "1",
    "gtmFired": "OK",
    "__cflb": "0H28vY1WcQgbwwJpSw5YiDRSJhpofbwsrRQEBw8VFLp",
    "usprivacy": "1YNN",
    "_imntz_error": "0",
    "r_p_s_n": "1",
    "_pbjs_userid_consent_data": "3524755945110770",
    "_lr_sampling_rate": "0",
    "geoC": "US",
    "OneTrustWPCCPAGoogleOptOut": "false",
    "adsFreeSalePopUp": "3",
    "smd": "895c36723c47b68fbda0436d7a7c1451-1721197665",
    "__cf_bm": "NPObEBgGXrUAmMXHavrpnGcUfl5Au.Bk.L5g3AVAJoo-1721197666-1.0.1.1-YHYG0flzFcKod.GDRKHxU6aU95WlS4KNipwLC4g9Zdjqxb0v.y1uD62Ttfb9.AmcJJxcXKmnQmL5OvTP3bbPBi7v1Mf8KDNuCDPuemwYmXw",
    "cf_clearance": "DVg8rYMyJFbPgtss3nbygxwBHhahCecprsDEMkD5jak-1721197669-1.0.1.1-kStVUuK3UjANinkSOo6.qe6f5qTXCyZsY_IYqqM6DlwZBYBaWh.2bzobVMrmyWocZLptYOH3vM4f4EnInQu16w",
    "PHPSESSID": "nnlr87gsr80eufgtl1aacqtuou",
    "browser-session-counted": "true",
    "user-browser-sessions": "4",
    "nyxDorf": "NjU%2BaTV9P2U3ZW99ZDU3NzZhM3YyMTM3",
    "__gads": "ID=c239539e8d014b5e:T=1721025202:RT=1721198389:S=ALNI_MZiyz1CJPWZeN_b1EOAYDbciJLVpQ",
    "__gpi": "UID=00000e9272a0461a:T=1721025202:RT=1721198389:S=ALNI_Mb2vk9x5SfyWHY43GNDnymtcuTfZA",
    "__eoi": "ID=0b6f60a76c39fcc8:T=1721025202:RT=1721198389:S=AA-AfjZry7tJi_EFENkWUWxc99YS",
    "invpc": "2",
    "_ga_C4NDLGKVMK": "GS1.1.1721197669.11.1.1721198435.8.0.0",
    "_ga": "GA1.1.2105063522.1721025196",
    "page_view_count": "2"
}



url = "https://www.investing.com/economic-calendar/Service/getCalendarFilteredData"
# 存放合并后的首页字段和详情页字段的列表
data_list = []
# 存放首页字段的队列
save_index_que = Queue()
# 存放详情页url的队列
save_detail_url_que = Queue()
from typing import List

# 存储详情页字段的队列
save_detail_que = Queue()
def get_data(page: str):
    data_one = "country%5B%5D=5&dateFrom=2024-06-01&dateTo=2024-07-15&timeZone=8&timeFilter=timeRemain&currentTab=custom&limit_from=0"
    data_two = "country%5B%5D=5&dateFrom=2024-06-01&dateTo=2024-07-15&timeZone=8&timeFilter=timeRemain&currentTab=custom&limit_from=1&pids%5B%5D=event-500169%3A&pids%5B%5D=event-499362%3A&pids%5B%5D=event-499367%3A&pids%5B%5D=event-499365%3A&pids%5B%5D=event-499363%3A&pids%5B%5D=event-499364%3A&pids%5B%5D=event-499366%3A&pids%5B%5D=event-500463%3A&pids%5B%5D=event-500464%3A&pids%5B%5D=event-500630%3A&pids%5B%5D=event-500476%3A&pids%5B%5D=event-500891%3A&pids%5B%5D=event-500892%3A&pids%5B%5D=event-499406%3A&pids%5B%5D=event-499405%3A&pids%5B%5D=event-499408%3A&pids%5B%5D=event-499404%3A&pids%5B%5D=event-500789%3A&pids%5B%5D=event-499407%3A&pids%5B%5D=event-500477%3A&pids%5B%5D=event-500574%3A&pids%5B%5D=event-500575%3A&pids%5B%5D=event-500576%3A&pids%5B%5D=event-500577%3A&pids%5B%5D=event-500578%3A&pids%5B%5D=event-499547%3A&pids%5B%5D=event-499556%3A&pids%5B%5D=event-499557%3A&pids%5B%5D=event-499562%3A&pids%5B%5D=event-499558%3A&pids%5B%5D=event-499559%3A&pids%5B%5D=event-499560%3A&pids%5B%5D=event-499561%3A&pids%5B%5D=event-500689%3A&pids%5B%5D=event-500752%3A&pids%5B%5D=event-500750%3A&pids%5B%5D=event-500751%3A&pids%5B%5D=event-500754%3A&pids%5B%5D=event-500749%3A&pids%5B%5D=event-500755%3A&pids%5B%5D=event-500757%3A&pids%5B%5D=event-500753%3A&pids%5B%5D=event-500756%3A&pids%5B%5D=event-500486%3A&pids%5B%5D=event-499713%3A&pids%5B%5D=event-500793%3A&pids%5B%5D=event-500422%3A&pids%5B%5D=event-500511%3A&pids%5B%5D=event-500512%3A&pids%5B%5D=event-500421%3A&pids%5B%5D=event-500423%3A&pids%5B%5D=event-499716%3A&pids%5B%5D=event-499719%3A&pids%5B%5D=event-499718%3A&pids%5B%5D=event-500631%3A&pids%5B%5D=event-500426%3A&pids%5B%5D=event-500424%3A&pids%5B%5D=event-500425%3A&pids%5B%5D=event-500709%3A&pids%5B%5D=event-500710%3A&pids%5B%5D=event-499828%3A&pids%5B%5D=event-499814%3A&pids%5B%5D=event-499826%3A&pids%5B%5D=event-499820%3A&pids%5B%5D=event-499818%3A&pids%5B%5D=event-499817%3A&pids%5B%5D=event-499830%3A&pids%5B%5D=event-499816%3A&pids%5B%5D=event-499831%3A&pids%5B%5D=event-499827%3A&pids%5B%5D=event-499833%3A&pids%5B%5D=event-499834%3A&pids%5B%5D=event-500708%3A&pids%5B%5D=event-500632%3A&pids%5B%5D=event-500428%3A&pids%5B%5D=event-500429%3A&pids%5B%5D=event-499836%3A&pids%5B%5D=event-500771%3A&pids%5B%5D=event-500772%3A&pids%5B%5D=event-500778%3A&pids%5B%5D=event-500775%3A&pids%5B%5D=event-500773%3A&pids%5B%5D=event-500765%3A&pids%5B%5D=event-500776%3A&pids%5B%5D=event-500763%3A&pids%5B%5D=event-500774%3A&pids%5B%5D=event-500779%3A&pids%5B%5D=event-500777%3A&pids%5B%5D=event-499930%3A&pids%5B%5D=event-500941%3A&pids%5B%5D=event-500850%3A&pids%5B%5D=event-500851%3A&pids%5B%5D=event-500854%3A&pids%5B%5D=event-499972%3A&pids%5B%5D=event-491110%3A&pids%5B%5D=event-500930%3A&pids%5B%5D=event-500933%3A&pids%5B%5D=event-501038%3A&pids%5B%5D=event-501146%3A&pids%5B%5D=event-500931%3A&pids%5B%5D=event-501039%3A&pids%5B%5D=event-501001%3A&pids%5B%5D=event-501002%3A&pids%5B%5D=event-501003%3A&pids%5B%5D=event-501004%3A&pids%5B%5D=event-501005%3A&pids%5B%5D=event-500121%3A&pids%5B%5D=event-500124%3A&pids%5B%5D=event-500125%3A&pids%5B%5D=event-500120%3A&pids%5B%5D=event-500122%3A&pids%5B%5D=event-500123%3A&pids%5B%5D=event-500127%3A&pids%5B%5D=event-500126%3A&pids%5B%5D=event-500128%3A&pids%5B%5D=event-501110%3A&pids%5B%5D=event-501108%3A&pids%5B%5D=event-501106%3A&pids%5B%5D=event-501104%3A&pids%5B%5D=event-501109%3A&pids%5B%5D=event-501105%3A&pids%5B%5D=event-501112%3A&pids%5B%5D=event-501111%3A&pids%5B%5D=event-501107%3A&pids%5B%5D=event-501103%3A&pids%5B%5D=event-501569%3A&pids%5B%5D=event-500134%3A&pids%5B%5D=event-500942%3A&pids%5B%5D=event-500141%3A&pids%5B%5D=event-500138%3A&pids%5B%5D=event-500137%3A&pids%5B%5D=event-500140%3A&pids%5B%5D=event-500139%3A&pids%5B%5D=event-500943%3A&pids%5B%5D=event-501035%3A&pids%5B%5D=event-472451%3A&pids%5B%5D=event-500944%3A&pids%5B%5D=event-500222%3A&pids%5B%5D=event-500225%3A&pids%5B%5D=event-500857%3A&pids%5B%5D=event-500224%3A&pids%5B%5D=event-500226%3A&pids%5B%5D=event-500856%3A&pids%5B%5D=event-500858%3A&pids%5B%5D=event-500223%3A&pids%5B%5D=event-500221%3A&pids%5B%5D=event-500861%3A&pids%5B%5D=event-500859%3A&pids%5B%5D=event-500860%3A&pids%5B%5D=event-500958%3A&pids%5B%5D=event-501279%3A&pids%5B%5D=event-500959%3A&pids%5B%5D=event-501149%3A&pids%5B%5D=event-501150%3A&pids%5B%5D=event-500974%3A&pids%5B%5D=event-500309%3A&pids%5B%5D=event-500975%3A&pids%5B%5D=event-500310%3A&pids%5B%5D=event-500317%3A&pids%5B%5D=event-500316%3A&pids%5B%5D=event-500318%3A&pids%5B%5D=event-500319%3A&pids%5B%5D=event-500320%3A&pids%5B%5D=event-500863%3A&pids%5B%5D=event-500864%3A&pids%5B%5D=event-500978%3A&pids%5B%5D=event-501269%3A&pids%5B%5D=event-501270%3A&pids%5B%5D=event-501276%3A&pids%5B%5D=event-501273%3A&pids%5B%5D=event-501271%3A&pids%5B%5D=event-501263%3A&pids%5B%5D=event-501274%3A&pids%5B%5D=event-501261%3A&pids%5B%5D=event-501272%3A&pids%5B%5D=event-501277%3A&pids%5B%5D=event-501275%3A&pids%5B%5D=event-501291%3A&pids%5B%5D=event-500395%3A&pids%5B%5D=event-501450%3A&pids%5B%5D=event-501451%3A&pids%5B%5D=event-501751%3A&pids%5B%5D=event-501452%3A&pids%5B%5D=event-501653%3A&pids%5B%5D=event-500438%3A&pids%5B%5D=event-500440%3A&pids%5B%5D=event-500439%3A&pids%5B%5D=event-500437%3A&pids%5B%5D=event-500436%3A&pids%5B%5D=event-501458%3A&pids%5B%5D=event-500444%3A&pids%5B%5D=event-500443%3A&pids%5B%5D=event-500445%3A&pids%5B%5D=event-500442%3A&pids%5B%5D=event-500447%3A&pids%5B%5D=event-501636%3A&pids%5B%5D=event-500446%3A&pids%5B%5D=event-501754%3A&pids%5B%5D=event-500633%3A&pids%5B%5D=event-501459%3A&submitFilters=0&last_time_scope=1718668800&byHandler=true"
    data_three = "country%5B%5D=5&dateFrom=2024-06-01&dateTo=2024-07-15&timeZone=8&timeFilter=timeRemain&currentTab=custom&limit_from=2&pids%5B%5D=event-501756%3A&pids%5B%5D=event-501637%3A&pids%5B%5D=event-501460%3A&pids%5B%5D=event-500449%3A&pids%5B%5D=event-500450%3A&pids%5B%5D=event-500448%3A&pids%5B%5D=event-500451%3A&pids%5B%5D=event-501461%3A&pids%5B%5D=event-501798%3A&pids%5B%5D=event-501799%3A&pids%5B%5D=event-501800%3A&pids%5B%5D=event-501801%3A&pids%5B%5D=event-501797%3A&pids%5B%5D=event-500581%3A&pids%5B%5D=event-500660%3A&pids%5B%5D=event-500659%3A&pids%5B%5D=event-501334%3A&pids%5B%5D=event-500668%3A&pids%5B%5D=event-500661%3A&pids%5B%5D=event-500658%3A&pids%5B%5D=event-501333%3A&pids%5B%5D=event-501335%3A&pids%5B%5D=event-500662%3A&pids%5B%5D=event-500663%3A&pids%5B%5D=event-500667%3A&pids%5B%5D=event-500666%3A&pids%5B%5D=event-500664%3A&pids%5B%5D=event-500665%3A&pids%5B%5D=event-500634%3A&pids%5B%5D=event-501641%3A&pids%5B%5D=event-501717%3A&pids%5B%5D=event-501721%3A&pids%5B%5D=event-501719%3A&pids%5B%5D=event-501714%3A&pids%5B%5D=event-501716%3A&pids%5B%5D=event-501713%3A&pids%5B%5D=event-501718%3A&pids%5B%5D=event-501720%3A&pids%5B%5D=event-501715%3A&pids%5B%5D=event-501336%3A&pids%5B%5D=event-501337%3A&pids%5B%5D=event-501480%3A&pids%5B%5D=event-501481%3A&pids%5B%5D=event-501643%3A&pids%5B%5D=event-501644%3A&pids%5B%5D=event-500741%3A&pids%5B%5D=event-500743%3A&pids%5B%5D=event-500742%3A&pids%5B%5D=event-500745%3A&pids%5B%5D=event-500746%3A&pids%5B%5D=event-500744%3A&pids%5B%5D=event-501505%3A&pids%5B%5D=event-501338%3A&pids%5B%5D=event-501339%3A&pids%5B%5D=event-502124%3A&pids%5B%5D=event-500841%3A&pids%5B%5D=event-501814%3A&pids%5B%5D=event-502005%3A&pids%5B%5D=event-502018%3A&pids%5B%5D=event-501736%3A&pids%5B%5D=event-501737%3A&pids%5B%5D=event-501743%3A&pids%5B%5D=event-501740%3A&pids%5B%5D=event-501738%3A&pids%5B%5D=event-501730%3A&pids%5B%5D=event-501741%3A&pids%5B%5D=event-501728%3A&pids%5B%5D=event-501739%3A&pids%5B%5D=event-501744%3A&pids%5B%5D=event-501742%3A&pids%5B%5D=event-502019%3A&pids%5B%5D=event-502128%3A&pids%5B%5D=event-500900%3A&pids%5B%5D=event-501878%3A&pids%5B%5D=event-500904%3A&pids%5B%5D=event-500906%3A&pids%5B%5D=event-500905%3A&pids%5B%5D=event-500903%3A&pids%5B%5D=event-500902%3A&pids%5B%5D=event-500901%3A&pids%5B%5D=event-500909%3A&pids%5B%5D=event-500908%3A&pids%5B%5D=event-500910%3A&pids%5B%5D=event-500907%3A&pids%5B%5D=event-500911%3A&pids%5B%5D=event-500912%3A&pids%5B%5D=event-501880%3A&pids%5B%5D=event-501881%3A&pids%5B%5D=event-501882%3A&pids%5B%5D=event-501883%3A&pids%5B%5D=event-501884%3A&pids%5B%5D=event-501977%3A&pids%5B%5D=event-501978%3A&pids%5B%5D=event-501979%3A&pids%5B%5D=event-501980%3A&pids%5B%5D=event-501981%3A&pids%5B%5D=event-501897%3A&pids%5B%5D=event-501898%3A&pids%5B%5D=event-501011%3A&pids%5B%5D=event-501010%3A&pids%5B%5D=event-502183%3A&pids%5B%5D=event-502189%3A&pids%5B%5D=event-502188%3A&pids%5B%5D=event-502187%3A&pids%5B%5D=event-502191%3A&pids%5B%5D=event-502184%3A&pids%5B%5D=event-502186%3A&pids%5B%5D=event-502190%3A&pids%5B%5D=event-502192%3A&pids%5B%5D=event-502185%3A&pids%5B%5D=event-501893%3A&pids%5B%5D=event-501894%3A&pids%5B%5D=event-501907%3A&pids%5B%5D=event-501096%3A&pids%5B%5D=event-501091%3A&pids%5B%5D=event-501100%3A&pids%5B%5D=event-501094%3A&pids%5B%5D=event-501098%3A&pids%5B%5D=event-501906%3A&pids%5B%5D=event-501092%3A&pids%5B%5D=event-501093%3A&pids%5B%5D=event-501089%3A&pids%5B%5D=event-501095%3A&pids%5B%5D=event-501099%3A&pids%5B%5D=event-501785%3A&pids%5B%5D=event-501789%3A&pids%5B%5D=event-501090%3A&pids%5B%5D=event-501088%3A&pids%5B%5D=event-501097%3A&pids%5B%5D=event-501908%3A&pids%5B%5D=event-501102%3A&pids%5B%5D=event-501101%3A&pids%5B%5D=event-501909%3A&pids%5B%5D=event-500635%3A&pids%5B%5D=event-501113%3A&pids%5B%5D=event-501114%3A&pids%5B%5D=event-501790%3A&pids%5B%5D=event-501791%3A&pids%5B%5D=event-501910%3A&pids%5B%5D=event-502026%3A&pids%5B%5D=event-502536%3A&pids%5B%5D=event-502624%3A&pids%5B%5D=event-502594%3A&pids%5B%5D=event-501931%3A&pids%5B%5D=event-501236%3A&pids%5B%5D=event-501237%3A&pids%5B%5D=event-501235%3A&pids%5B%5D=event-501233%3A&pids%5B%5D=event-501231%3A&pids%5B%5D=event-501234%3A&pids%5B%5D=event-501232%3A&pids%5B%5D=event-502668%3A&pids%5B%5D=event-502676%3A&pids%5B%5D=event-501247%3A&pids%5B%5D=event-501249%3A&pids%5B%5D=event-501253%3A&pids%5B%5D=event-501250%3A&pids%5B%5D=event-501251%3A&pids%5B%5D=event-501252%3A&pids%5B%5D=event-500636%3A&pids%5B%5D=event-502129%3A&pids%5B%5D=event-501783%3A&pids%5B%5D=event-501784%3A&pids%5B%5D=event-502316%3A&pids%5B%5D=event-502317%3A&pids%5B%5D=event-502318%3A&pids%5B%5D=event-502319%3A&pids%5B%5D=event-502320%3A&pids%5B%5D=event-502321%3A&pids%5B%5D=event-502322%3A&pids%5B%5D=event-502323%3A&pids%5B%5D=event-502324%3A&pids%5B%5D=event-502325%3A&pids%5B%5D=event-502326%3A&pids%5B%5D=event-502795%3A&pids%5B%5D=event-502796%3A&pids%5B%5D=event-502797%3A&pids%5B%5D=event-502798%3A&pids%5B%5D=event-502800%3A&pids%5B%5D=event-502799%3A&pids%5B%5D=event-502801%3A&pids%5B%5D=event-502802%3A&pids%5B%5D=event-502803%3A&pids%5B%5D=event-502804%3A&pids%5B%5D=event-502806%3A&pids%5B%5D=event-502805%3A&pids%5B%5D=event-502215%3A&pids%5B%5D=event-501397%3A&pids%5B%5D=event-501398%3A&pids%5B%5D=event-501402%3A&pids%5B%5D=event-501399%3A&pids%5B%5D=event-501400%3A&pids%5B%5D=event-501401%3A&pids%5B%5D=event-502338%3A&pids%5B%5D=event-502339%3A&pids%5B%5D=event-502254%3A&pids%5B%5D=event-502401%3A&pids%5B%5D=event-502402%3A&pids%5B%5D=event-501427%3A&pids%5B%5D=event-502403%3A&submitFilters=0&last_time_scope=1719878400&byHandler=true"
    data_dict = {"1": data_one, "2": data_two, "3": data_three}
    data = data_dict[page]
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    res = response.json()['data']
    tree = etree.HTML(res)
    data1 = tree.xpath('//tr[@class="js-event-item "]')
    data2 = tree.xpath('//tr[@class="js-event-item revised"]')
    for i1 in data1:
        detail_url1 = "https://www.investing.com" + i1.xpath('./td[4]/a/@href')[0]

        b = {"时间": i1.xpath('./@data-event-datetime')[0],
             "货币": i1.xpath('./td[2]/text()')[0].strip(),
             "活动": i1.xpath('./td[4]/a/text()')[0].strip(),
             "今值": i1.xpath('./td[5]/text()')[0].strip(),
             "预测值": i1.xpath('./td[6]/text()')[0].strip(),
             "前值": i1.xpath('./td[7]/span/text()')[0].strip(),
             }
        # 把首页的字段添加到存放首页字段的队列
        save_index_que.put(b)

        # 把详情页的URL添加到存放详情页url的队列
        save_detail_url_que.put(detail_url1)

    for i2 in data2:
        c = {"时间": i2.xpath('./@data-event-datetime')[0].strip(),
             "货币": i2.xpath('./td[2]/text()')[0].strip(),
             "活动": i2.xpath('./td[4]/a/text()')[0].strip(),
             "今值": i2.xpath('./td[5]/text()')[0].strip(),
             "预测值": i2.xpath('./td[6]/text()')[0].strip(),
             "前值": i2.xpath('./td[7]/span/text()')[0].strip(),
             }

        detail_url2 = "https://www.investing.com" + i2.xpath('./td[4]/a/@href')[0]

        save_detail_url_que.put(detail_url2)
        save_index_que.put(c)

def parse_detail_url():
    while 1:
        # 从队列中取出详情页url
        detail_url = save_detail_url_que.get()
        res2 = requests.get(detail_url, headers=headers, cookies=cookies)

        tree = etree.HTML(res2.text)
        b = {"最新发布": tree.xpath('//*[@id="releaseInfo"]/span[1]/div/text()')[0].strip() if tree.xpath(
            '//*[@id="releaseInfo"]/span[1]/div/text()') else "",
             "来源": tree.xpath(
                 '//div[@id="overViewBox"]/div[@class="clear"]/preceding-sibling::div[1]/div[4]/span[2]/a/text()')[
                 0].strip() if
             tree.xpath(
                 '//div[@id="overViewBox"]/div[@class="clear"]/preceding-sibling::div[1]/div[4]/span[2]/a/text()') else "",
             "info": tree.xpath('//div[@class="left"]/text()')[0] if tree.xpath('//div[@class="left"]/text()') else ""}
        # 详情页的字段存放队列
        save_detail_que.put(b)
        # 从队列取出详情页url后让计数减一
        save_detail_url_que.task_done()


def save_data():
    while 1:
        a = save_detail_que.get()
        b = save_index_que.get()
        # 合并首页字段和详情页字段
        b.update(a)
        # 把合并的首页字段和详情页字段添加到列表
        data_list.append(b)
        save_detail_que.task_done()
        save_index_que.task_done()


def main():
    """
    输入：
        获取美国指定日期需要从网站上筛选然后提取表单字符串
        写入字典 {"page":"page_data_str"}
        传入page 取值
        具体看代码77-81行

    输出：json文件
        """
    start_time = time.time()
    # 把所有的详情页url放到队列
    for page in range(1, 4):
        get_data(str(page))
    thread_list = []
    for thread_num in range(20):
        t = threading.Thread(target=parse_detail_url)
        thread_list.append(t)
    for thread_num1 in range(20):
        t2 = threading.Thread(target=save_data)
        thread_list.append(t2)

    for i in thread_list:
        # 设置守护线程
        i.setDaemon(True)
        i.start()
    for q in [save_detail_url_que, save_index_que]:
        q.join()  # 让主线程阻塞，等待队列的计数为0
    with open('../commit/investing_english.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data_list, ensure_ascii=False, indent=4))
    end_time = time.time()
    consume_time = end_time - start_time
    print(f"程序耗时{consume_time}秒")


if __name__ == '__main__':
    main()


