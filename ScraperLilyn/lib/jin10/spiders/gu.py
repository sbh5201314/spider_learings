import scrapy
from scrapy.http import HtmlResponse
from scrapy import cmdline

from datetime import datetime, timedelta


def timestamp_to_time(timestamp):
    # 将时间戳转换为datetime对象
    dt_object = datetime.fromtimestamp(timestamp)

    # 格式化输出时间
    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_time


class GuSpider(scrapy.Spider):
    name = "gu"

    # allowed_domains = ["xx.com"]
    # start_urls = ["https://www.baidu.com"]
    def start_requests(self):
        # 设置开始日期和结束日期
        start_date = datetime(2024, 6, 1)  # 7月1日
        end_date = datetime(2024, 7, 16)  # 7月16日，但不包括该日期

        # 循环输出7月份的日期
        current_date = start_date
        while current_date < end_date:
            date = current_date.strftime('%Y/%m/%d')  # 格式化输出日期为 YYYY/MM/DD
            # 将日期字符串分割成年、月、日
            year, month, day = date.split('/')

            # 构建新的日期字符串
            new_date_str = f"2024/daily/{month}/{day}"

            url = f"https://cdn-rili.jin10.com/web_data/{new_date_str}/economics.json"

            current_date += timedelta(days=1)  # 增加一天，继续循环
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        try:
            for i in response.json():
                if i['country'] == "美国":
                    time = timestamp_to_time(i['pub_time_unix'])
                    id = i['id']
                    detail_url = f"https://rili.jin10.com/detail/{id}"
                    yield scrapy.Request(url=detail_url, callback=self.parse_detail,
                                         meta={"时间": time, "数据": i['country'] + i['time_period'] + i['name'],
                                               "重要性": i['star']
                                               })
        except Exception as e:
            print("出错了")

    def parse_detail(self, response):

        c = {"最新发布": response.xpath(
            "//div[@class='detail-page']/div[2]/div[1]/div[2]/text()").extract_first().strip().replace("--", ""),
             "公布值": response.xpath(
                 "//div[@class='detail-page']/div[2]/div[2]/div[2]/text()").extract_first().strip().replace("--", ""),
             "预测值": response.xpath(
                 "//div[@class='detail-page']/div[2]/div[3]/div[2]/text()").extract_first().strip().replace("--", ""),
             "前值": response.xpath(
                 "//div[@class='detail-page']/div[2]/div[4]/div[2]/text()").extract_first().strip().replace("--", ""),
             "下次公布时间": response.xpath(
                 "//div[@class='detail-page']/div[2]/div[5]/div[2]/text()").extract_first().strip().replace("--", ""),
             "发布频率": response.xpath(
                 "//div[@class='detail-page']/div[2]/div[6]/div[2]/text()").extract_first().strip().replace("--", ""),
             "数据释义": response.xpath(
                 "//div[@class='detail-page']/table/tbody/tr[1]/td[2]/text()").extract_first().strip().replace("--",
                                                                                                               ""),
             "数据影响": response.xpath(
                 "//div[@class='detail-page']/table/tbody/tr[2]/td[2]/text()").extract_first().strip().replace("--",
                                                                                                               ""),
             "统计方法": response.xpath(
                 "//div[@class='detail-page']/table/tbody/tr[3]/td[2]/text()").extract_first().strip().replace("--",
                                                                                                               ""),
             "公布机构": response.xpath(
                 "//div[@class='detail-page']/table/tbody/tr[4]/td[2]/text()").extract_first().strip().replace("--",
                                                                                                               "")}
        b = {"时间": response.meta['时间'], "数据": response.meta['数据'], "重要性": response.meta['重要性']}
        b.update(c)
        yield b


if __name__ == '__main__':
    """
    输入:
    start_date = datetime(2024, 6, 1)  # 7月1日
    end_date = datetime(2024, 7, 16)  # 7月16日，但不包括该日期
    把首尾日期修改即可  
    输出:
    json文件 
    
    """
    cmdline.execute('scrapy crawl gu --nolog'.split())
