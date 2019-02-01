
# coding : utf-8

from flask import Flask, current_app, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__,
            static_url_path= "/python",
            static_folder="static",
            template_folder="templates")

class MyConfig(object):
    DEBUG = True
    ITCAST = "python"

# 1. same route: multiple view functions
# @app.route("/")
# def hello():
#     # app: is a global variable; to use in a function locally, use current_app
#     print(current_app.config.get("ITCAST"))
#     return "hello itcast 1"
#
# @app.route("/")
# def hello2():
#     return "hello itcast 2"
#

# 2. same function, multiple routes
@app.route("/index")
@app.route("/hi")
def index():
    return "index page"

@app.route("/post", methods=['GET', 'POST'])
def post_only():
    return "post_only final"

@app.route("/redirect")
def redirect():
    return '<a href="%s">post only</a>' % url_for("post_only")


app.config.from_pyfile("MyConfig.cfg")
# app.config.from_object(debug==True)


# customize routing converter
@app.route("/<name>")
def hello(name):
    return "hello %s" % name

@app.route("/<int:id>")
def hello_id(id):
    return "hello id=%d" % id

@app.route("/<float:id>")
def hello_idFloat(id):
    return "hello id=%s" % id

class ReConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(ReConverter, self).__init__(url_map)
        # assign regex(1st in args list) to the regex property of self object
        self.regex = args[0]

    def to_python(self, value):
        '''regex params--> to_python()-->return values, pass to views function'''
        print(u"to_python() has been called, value=%s" % value)
        return value

    def to_url(self, value):
        '''python params--> url: used'''
        print(u"to_url() has been called, value=%s" % value)
        return value


# app's url_map mapping: converters is a dict:
app.url_map.converters["re"] = ReConverter

@app.route("/id/<re('\d{3}'):id>")
def hello_re(id):
    return "customized hello id=%s" % id

@app.route("/itcast")
def itcast():                           # url_for(endpoint, **value)
    return '<a href="%s">hello_re</a>' % url_for("hello_re", id="123")

if __name__ == '__main__':
    #app.run(MyConfig)
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)