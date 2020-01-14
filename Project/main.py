# coding=utf-8
from scrapy_plus.core.engine import Engine  # 导入引擎

# from spiders.baidu import BaiduSpider
# from spiders.qiubai import QiubaiSpider
# from pipelines import BaiduPipeline,QiubaiPipeline
# from spider_middlewares import TestSpiderMiddleware1,TestSpiderMiddleware2
# from downloader_middlewares import TestDownloaderMiddleware2,TestDownloaderMiddleware1

if __name__ == '__main__':
    # 实例化百度爬虫
    # baidu = BaiduSpider()
    # qiubai = QiubaiSpider()
    # spdiers = {baidu.name:baidu,qiubai.name:qiubai}
    # pipelines = [BaiduPipeline(),QiubaiPipeline()]
    # spider_mids = [TestSpiderMiddleware2(),TestSpiderMiddleware1()]
    # downloader_mids = [TestDownloaderMiddleware1(),TestDownloaderMiddleware2()]
    # engine = Engine(spdiers,pipelines,spider_mids,downloader_mids) #实例化引起
    engine = Engine()
    engine.start()  # 启动引擎
