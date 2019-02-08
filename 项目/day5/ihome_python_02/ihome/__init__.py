# coding: utf-8

# 这是项目的init文件
import redis
import logging

from flask import Flask
from config import config_dict
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from logging.handlers import RotatingFileHandler


# 业务逻辑都写在这里, manage.py只是启动脚本, 创建真正要用的app在这里创建

# 都放在外面是因为其他的地方要用到, 不能写在函数中
# 构建数据库对象
db = SQLAlchemy()

# 构建redis连接对象
redis_store = None

# 因为CSRFProtect()只是提供防护,但是生成csrf_token还是后面需要自己做
csrf = CSRFProtect()

# 1. 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)
# 2. 创建日志记录器
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024, backupCount=10)
# 3. 创建日志记录的格式
format = logging.Formatter('%(levelname)s %(filename)s: %(lineno)d %(message)s')
# 4. 为刚刚创建的日志记录器设置记录的格式
file_log_handler.setFormatter(format)
# 5. 为全局的日志工具对象 (flask app使用的) 添加日志记录器
logging.getLogger().addHandler(file_log_handler)

# 工厂模式创建app: 根据不同的需求创建不同配置信息的app, 不自己手动创建
def create_app(config_name):

    app = Flask(__name__)

    conf = config_dict[config_name]
    app.config.from_object(conf)

    db.init_app(app) # 初始化db对象

    global redis_store
    redis_store = redis.StrictRedis(
        host=conf.REDIS_HOST, port=conf.REDIS_PORT)  # 创建用来保session的redis实例

    csrf.init_app(app)

    # 将flask的session数据保存到redis中
    # 因为后面不需要操作Session对象, 只是改变flask的session机制
    Session(app)

    # 3. 注册蓝图路由
    import api_v1_0
    app.register_blueprint(api_v1_0.api, url_prefix = "/api/v1_0")

    return app
