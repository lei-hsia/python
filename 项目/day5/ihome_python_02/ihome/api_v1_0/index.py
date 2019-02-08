# coding: utf-8

from . import api
from ihome import db
import logging
from flask import current_app

# 2. 蓝图路由装饰视图函数     (视图函数中肯定会有数据库的操作)
@api.route("/index")
def index():
    # logging.error("dfg")
    # logging.warn("")
    # logging.info("")
    # logging.debug("")
    current_app.logger.error("ERROR MSG")
    current_app.logger.warn("WARN MSG")
    current_app.logger.info("INFO MSG")
    current_app.logger.debug("DEBUG MSG")
    return "index page"