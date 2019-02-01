
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