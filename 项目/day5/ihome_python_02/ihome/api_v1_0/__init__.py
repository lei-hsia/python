# coding: utf-8

from flask import Blueprint

# 1. 创建蓝图对象
api = Blueprint("api", __name__)

# 这样, 注册蓝图之后app也能知道视图函数的存在
from . import index

