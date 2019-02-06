from . import app_cart_obj
from flask import render_template

@app_cart_obj.route("/get_cart")
def get_cart():
    return render_template("cart.html")