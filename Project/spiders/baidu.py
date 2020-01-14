# coding=utf-8
from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item
import urllib.parse

# class BaiduSpider(Spider):
#     name = "baidu"
#     start_urls = ["http://www.baidu.com"]*3
#
#
#     def parse(self,response):
#         yield Item(response.body[:10])


import time

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item
import js2py


class SinaGunDong(Spider):
    name = "sina_gundong"

    def start_requests(self):
        while True:
            # 需要发起这个请求，才能获取到列表页数据，并且返回的是一个js语句
            url = "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&ch=&k=&offset_page=0&offset_num=0&num=120&asc=&page=1&r=0.5559616678192825"
            yield Request(url, parse='parse', filter=False)
            time.sleep(10)  # 每10秒发起一次请求

    def parse(self, response):
        '''响应体数据是js代码'''
        # 使用js2py模块，执行js代码，获取数据
        ret = js2py.eval_js(response.body.decode("gbk"))  # 对网站分析发现，数据编码格式是gbk的，因此需要先进行解码
        yield Item(ret.list)


if __name__ == '__main__':
    sina = SinaGunDong()
    for i in sina.start_requests():
        print(i.url)
