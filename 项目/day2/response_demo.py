
from flask import Flask, config, make_response

app = Flask(__name__)

class MyConfig():
    DEBUG = True

app.config.from_object(MyConfig)

@app.route('/')
def index():
    ''' 1. (response, status code:don't need to be standard, headers) '''
    #return "index page", "666 itcast python", [("itcast","python"), ("city", "shenzhen")]
    #return "index page", "666 itcast python", {"itcast1": "python1"}

    # 2. make_response
    resp = make_response("index page itcast python")  # response
    resp.status = "666 status code"  # status
    resp.headers["sample key"] = "sample value"
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)