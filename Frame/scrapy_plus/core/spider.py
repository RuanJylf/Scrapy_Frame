# coding=utf-8
# 爬虫
from scrapy_plus.http.request import Request
from scrapy_plus.item import Item


class Spider:
    '''完成对spider的封装'''
    start_urls = []  # 爬虫最开启请求的url地址

    def start_requests(self):
        '''
        构造start_url地址的请求
        :return: request
        '''
        for url in self.start_urls:
            yield Request(url)

    def parse(self, response):
        '''
        默认处理start_url地址对应的响应
        :param response: response对象
        :return: item或者是request
        '''
        yield Item(response.body)
