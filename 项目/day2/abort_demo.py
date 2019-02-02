
from flask import Flask, config, abort, make_response

'''
1. abort() function: ~raise: exception, stop executing
2. @app.errorhandler(): route: customize error msg
'''
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

# don't use the error page provided by flask: customize what users would see
@app.errorhandler(404)
def handler_404(e):
    return "error code: %s" % e


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)