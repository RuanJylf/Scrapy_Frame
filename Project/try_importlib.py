# coding=utf-8
import importlib
from scrapy_plus.item import Item

PIPELINES = [
    'pipelines.BaiduPipeline',
    'pipelines.QiubaiPipeline'
]

SPIDERS = [
    'spiders.baidu.BaiduSpider',
    'spiders.qiubai.QiubaiSpider'
]

for pipeline in SPIDERS:
    module_name = pipeline.rsplit(".", 1)[0]  # module的名字，路径
    cls_name = pipeline.rsplit(".", 1)[-1]  # 类名

    module = importlib.import_module(module_name)  # 导入module

    cls = getattr(module, cls_name)  # 获取module下的类

    # cls().process_item(Item("a"),"a")
    print(cls().name)
