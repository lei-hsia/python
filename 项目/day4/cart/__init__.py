# coding:utf-8
from flask import Blueprint

# 1. 创建一个蓝图对象
app_cart_obj = Blueprint("app_cart_name", __name__, template_folder="templates")

# 2. 创建蓝图路由并导入
from .views import get_cart
