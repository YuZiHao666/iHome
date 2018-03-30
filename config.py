# -*- coding: utf-8 -*-
import redis


class Config(object):
    '''加载配置'''
    DEBUG = True

    # 配置安全秘钥：CSRF基于session的，所以需要配置安全秘钥
    SECRET_KEY = 'qwertyasdfghzxcvbnpoiuytrlkjhgfmnbvcx'

    # 配置mysql数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 配置session存储数据的redis
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启数据签名 让session数据不以明文形式存储
    SESSION_USE_SIGNER = True
    # 设置超时时长
    PERMANENT_SESSION_LIFETIME = 86400  # 单位是秒
