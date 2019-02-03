
from flask import Flask, render_template

app = Flask(__name__)

# customize filter
def filter_list_2(li):
    return li[::2]

app.add_template_filter(filter_list_2, "li_2")

# 2. customize filter
@app.template_filter("li_3")
def filter_list_3(li):
    return li[::3]

@app.route("/")
def index_fun():

    my_dict = {
        "first name" : "lei",
        "last_name" : "xia"
    }
    my_list = [1,2,3,4,5,6]
    my_int = 0

    content = {
        "name" : "python",
        "age" : 24,
        "my_dict": my_dict,
        "my_list" : my_list,
        "my_int" : my_int,
        "nested" : my_list[my_int]
    }
    return render_template("index.html", **content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)