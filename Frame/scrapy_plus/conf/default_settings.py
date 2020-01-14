# coding=utf-8
import logging

# log默认的配置
DEFAULT_LOG_LEVEL = logging.INFO  # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'  # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'  # 默认日志文件名称

# 设置并发的数量
COCOURRENT_REQUEST = 5

# 选择线程池的方式
ASYNC_TYPE = "courtine"  # thread

# 设置是否需要持久化，和分布式
SCHEDULER_PERSIST = True

# redis队列默认配置
REDIS_QUEUE_NAME = 'request_queue'
REDIS_QUEUE_HOST = 'localhost'
REDIS_QUEUE_PORT = 6379
REDIS_QUEUE_DB = 0
# redis指纹集合的位置，存储指纹
REDIS_SET_NAME = "redis_set"
REDIS_SET_HOST = "localhost"
REDIS_SET_PORT = 6379
REDIS_SET_DB = 0

# redi备份的位置
REDIS_BACKUP_NAME = "redis_backup"
REDIS_BACKUP_HOST = "localhost"
REDIS_BACKUP_PORT = 6379
REDIS_BACKUP_DB = 0
