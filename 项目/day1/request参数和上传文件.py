
from flask import Flask, request

app = Flask(__name__)

class MyConfig(object):
    DEBUG = True
    ITCAST = 'python'

app.config.from_object(MyConfig)

# extrieve params from request object
# common request properties: data, form, args, cookies, headers, method, url, files
@app.route("/")
def hello():
    # not:  request.GET["name"], because it could be there's no property "name"; using request.args.get(): return null
    name = request.args.get("name")
    return "hello %s" % name


@app.route("/upload", methods=["POST"])
def upload():
    pic_file = request.files.get("pic") # get file uploaded by user
    if pic_file:
    # save to local server
    # pic_data = pic_file.read()
    # with open("./upload_image", "wb") as f:
    #     f.write(pic_data)
        pic_file.save("./upload_image")
        return "success"
    else:
        return "miss pic_file"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)