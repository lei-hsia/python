# coding: utf-8
import redis

class Config():

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:5000/ihome_python_02"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    SECRET_KEY = "n32043rij3*^!#(H)HF#I@_(FJg"

    # session配置信息
    SESSION_TYPE = "redis"  # 指明保存到redis中
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # session保存到的redis实例
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400  # seconds


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    '''图简便, 这里不写东西'''

config_dict = {
    "develop" : DevelopmentConfig,
    "product" : ProductionConfig
}