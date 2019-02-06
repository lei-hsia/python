# coding: utf-8
from flask import Flask
from register import register
from get_goods import get_goods
from orders import app_orders_BP_obj
from cart import app_cart_obj

app = Flask(__name__)

@app.route("/")
def index():
    return "index page gunicorn"

app.route("/register")(register)
app.route("/get_goods")(get_goods)

#. 3. 在程序中注册蓝图
app.register_blueprint(app_orders_BP_obj, url_prefix = "/orders")
app.register_blueprint(app_cart_obj, url_prefix = "/cart")

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)