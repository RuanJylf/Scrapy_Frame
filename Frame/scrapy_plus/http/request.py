# coding=utf-8
# 请求对象


class Request:
    '''完成对请求对象的封装'''

    def __init__(self, url, method="GET", headers=None, params=None, \
                 data=None, parse="parse", meta=None, filter=True):
        '''
        初始化request对象
        :param url: url地址
        :param method: 请求方法
        :param headers: 请求头
        :param params: 请求的参数
        :param data: 请求体
        :param parse: 请求对象响应的处理函数的函数名
        :param meta: 字典：不同的解析函数间传递数据
        '''
        self.url = url
        self.method = method
        self.headers = headers
        self.params = params
        self.data = data
        self.parse = parse
        self.meta = meta
        self.filter = filter  # 默认会进行请求去重，如果为False，不进行去重
        self.retry_time = 0
