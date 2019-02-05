
from flask import Flask, make_response, jsonify, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/person")
def get_person():
    '''get person info in form of json''' 
    # jsonify()参数是一个dict,字典中包含了需要的信息
    p = {
        "name": "zhangsan",
        "age" : 24
    }
    # resp = make_response(json.dumps(p))
    # resp.status = "person customized status"
    # resp.headers["Content-Type"] = "application/json"
    # return resp
    return jsonify(p)  # jsonify finishes: wrap string to json, with status code and headers info

@app.route("/login")
def login():
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
