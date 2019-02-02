
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    '''essence: +1 Cookie in the response header; cookie: set in headers so as to let frontend know'''
    resp = make_response("success")
    resp.set_cookie("sample_key", "sample_value")
    resp.set_cookie("itcast", "python", max_age = 3600)
    resp.headers["itcast2"] = "python2"
    resp.headers["Set-Cookie"] = "itcast=python; Expires=Fri, 01-Feb-2019 21:50:35 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    cookie = request.cookies.get("itcast")
    return cookie

@app.route("/del_cookie")
def del_cookie():
    resp = make_response("success")
    # resp's delete_cookie : only change the expiration date of this cookie
    resp.delete_cookie("itcast")
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)