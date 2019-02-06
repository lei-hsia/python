# coding: utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    # 接收参数
    user_name = request.form.get("username")
    password = request.form.get("password")
    # 参数判断　从而决定给前端返回什么json值
    if not all([user_name, password]):
        resp = {
            "code": 1,
            "msg": "invalid params"
        }
        return jsonify(resp)

    if user_name == "admin" and password == "python":  # suppose this name/pass
        resp = {
            "code": 0,
            "msg": "login success"
        }
        return jsonify(resp)
    else :
        resp = {
            "code": 2,
            "msg": "wrong username/password"
        }
        return jsonify(resp)