

from flask import Flask, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "sfgtjj23456y9h5jiegnv129(!&(#"

@app.route("/login_set_session")
def login_set_session():
    session["name"] = "python"  # save session data
    session["age"] = 18
    return "login... set session success"

@app.route("/")
def index():
    content1 = session.get("name")
    content2 = session.get("age")
    return "hello %s age %s" % (content1, content2)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)