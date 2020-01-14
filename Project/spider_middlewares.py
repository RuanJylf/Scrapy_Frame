# coding=utf-8

class TestSpiderMiddleware1:
    '''实现爬虫中间件'''

    def process_request(self, request):
        '''
        处理请求
        :param request:请求
        :return: 请求
        '''
        # print("TestSpiderMiddleware1 -- process_request")
        return request

    def process_response(self, response):
        '''
        处理response
        :param response:response
        :return:response
        '''
        # print("TestSpiderMiddleware1 -- process_response")
        return response


class TestSpiderMiddleware2:
    '''实现爬虫中间件'''

    def process_request(self, request):
        '''
        处理请求
        :param request:请求
        :return: 请求
        '''
        # print("TestSpiderMiddleware2 -- process_request")
        return request

    def process_response(self, response):
        '''
        处理response
        :param response:response
        :return:response
        '''
        # print("TestSpiderMiddleware2 -- process_response")
        return response
