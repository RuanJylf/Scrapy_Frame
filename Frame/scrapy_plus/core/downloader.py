# coding=utf-8
# 下载器
import requests

from scrapy_plus.http.response import Response
from scrapy_plus.utils.log import logger


class Downloader:
    '''完成对下载器对象的封装'''

    def get_response(self, request):
        '''
        实现结构请求对象，发送请求，获取响应
        :param request: 请求对象
        :return: resposne对象
        '''
        if request.method.upper() == "GET":
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == "POST":
            resp = requests.post(request.url, headers=request.headers, params=request.params, data=request.data)
        else:
            raise Exception("不支持的请求方法：<{}>".format(request.method))
        logger.info("<{} {}>".format(resp.status_code, resp.request.url))
        return Response(url=resp.url, body=resp.content, headers=resp.headers, status_code=resp.status_code)
