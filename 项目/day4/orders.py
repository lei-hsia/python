# coding: utf-8
from flask import Blueprint

# 1.　创建蓝图对象
app_orders_BP_obj = Blueprint("nameBP", __name__)

#. 2. 注册蓝图路由
@app_orders_BP_obj.route("/get_orders")
def get_orders():
    return "get orders page"

