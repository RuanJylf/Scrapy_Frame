# coding=utf-8
# 调度器
from six.moves.queue import Queue
import w3lib.url
from hashlib import sha1
import six
from scrapy_plus.utils.log import logger
from scrapy_plus.utils.queue import Queue as RedisQueue
from scrapy_plus.conf.settings import SCHEDULER_PERSIST, MAX_RETRY_TIME
from scrapy_plus.utils.set import NoramlFilterContainer, RedisFilterContainer
from scrapy_plus.utils.redis_hash import RedisBackupRequest


def _to_bytes(string):
    if six.PY2:  # 当环境是python2
        if isinstance(string, str):
            return string
        else:
            return string.encode("utf-8")  # unicode类型转化为字节类型
    elif six.PY3:  # 当环境是python3
        if isinstance(string, str):
            return string.encode("utf-8")
        else:
            return string


class Scheduler:
    '''完成调取器模块的封装'''

    def __init__(self, collector):
        if not SCHEDULER_PERSIST:
            self.queue = Queue()  # 存储的是带抓取的请求
            # 不适用分布式的时候，使用python的集合存储指纹
            self._filter_container = NoramlFilterContainer()
        else:
            # 当决定要是用分布式的时候，使用redis队列
            self.queue = RedisQueue()
            # 使用分布式的时候，redis的集合存储指纹
            self._filter_container = RedisFilterContainer()

        # self._filter_container = set() #保存指纹的集合
        self.collector = collector
        # self.repeat_request_nums = 0 #统计请求重复的数量
        self.request_backup = RedisBackupRequest()

    def add_request(self, request):
        '''
        实现添加request到队列中
        :param request: 请求对象
        :return: None
        '''
        # 判断请求是否需要进行去重，如果不需要，直接添加到队列
        if not request.filter:  # 不需要去重
            request.fp = self._gen_fp(request)
            self.queue.put(request)
            logger.info("添加不去重的请求<{} {}>".format(request.method, request.url))
            return

        if self._filter_request(request):
            self.queue.put(request)
            if SCHEDULER_PERSIST:
                self.request_backup.save_request(request.fp, request)

    def get_request(self):
        '''
        实现获取队列中的request对象
        :return: 请求对象
        '''
        try:
            request = self.queue.get(block=False)
        except:
            return None
        else:
            if request.filter and SCHEDULER_PERSIST:
                if request.retry_time >= MAX_RETRY_TIME:
                    self.request_backup.delete_request(request.fp)
                request.retry_time += 1
                self.request_backup.save_request(request.fp, request)
            return request

    def add_lost_request(self):
        if SCHEDULER_PERSIST:
            for request in self.request_backup.get_requests():
                # 之前已经添加过指纹，备份容器恢复的时候，需要先把指纹删除
                self._filter_container.delete_fp(request.fp)
                # 对之前添加过的请求数量进行-1
                # self.collector.decr(self.collector.request_nums_key)
                self.queue.put(request)

    def _filter_request(self, request):
        '''
        实现判断请求是够重复
        :param request: 请求对象
        :return: bool
        '''

        # 给request对象添加一个fp属性，保存指纹
        request.fp = self._gen_fp(request)
        if not self._filter_container.exists(request.fp):  # 判断指纹不在指纹机集合中
            # 把指纹添加到指纹集合中
            self._filter_container.add_fp(request.fp)
            return True
        else:
            logger.info("发现重复的请求:<{} {}>".format(request.method, request.url))
            # self.repeat_request_nums += 1
            self.collector.incr(self.collector.repeat_request_nums_key)

    def _gen_fp(self, request):
        '''
        生成request对象的指纹
        :param request:request对象
        :return: 指纹字符串
        '''
        # 对url地址，请求体，请求参数，请求方法进行加密，得到指纹
        # 对url地址进行排序
        url = w3lib.url.canonicalize_url(request.url)
        # 请求方法
        method = request.method.upper()
        # 请求的参数
        params = request.params if request.params is not None else {}
        params = str(sorted(params.items(), key=lambda x: x[0]))

        # 请求体排序
        data = request.data if request.data is not None else {}
        data = str(sorted(data.items(), key=lambda x: x[0]))

        # 使用sha1对数据进行加密
        fp = sha1()
        # 添加url地址
        fp.update(_to_bytes(url))
        # 添加请求方法
        fp.update(_to_bytes(method))
        # 添加请求参数
        fp.update(_to_bytes(params))
        # 添加请求体
        fp.update(_to_bytes(data))

        return fp.hexdigest()  # 返回16进制字符串
