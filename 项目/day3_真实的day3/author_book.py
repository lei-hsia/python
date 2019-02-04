
# coding: utf-8
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class MyConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book_02"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = "nfh3923it3hguwf&%^T&(GIB"

app.config.from_object(MyConfig)

db = SQLAlchemy(app)

class Author(db.Model):
    __tablename__ = "tbl_author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # backref: 是book表对应的字段名
    books = db.relationship("Book", backref = "author") # 这里不是表　所以不用去表底层

class Book(db.Model):
    __tablename__ = "tbl_book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_author.id")) # 设置外键是表底层: 表名是tbl_author

# 创建表单类
class AuthorBookForm(FlaskForm):
    author_name = StringField(label=u"作者", validators=[DataRequired()]) # validators传入列表,里面传递的参数是类对象
    book_name = StringField(label=u"书籍", validators=[DataRequired()])
    submit = SubmitField(label=u"提交")


@app.route("/", methods=["GET", "POST"]) # 因为表单提交数据的方式是POST方式提交的,所以请求的方式要改
def index():
    form = AuthorBookForm() # 表单类定义完了是不够的,因为能看到的东西取决于视图函数,所以要创建一个表单类的对象
    if form.validate_on_submit():
        # 表单数据验证成功
        # 保存进数据库:
        # 具体做法: 先从表单拿到数据, 再根据拿到的数据创建对象, 保存进数据库; 这里首先要保存Author类对象才能再保存Book类对象
        author_name = form.author_name.data
        book_name = form.book_name.data

        author_obj = Author(name = author_name)
        db.session.add(author_obj)
        db.session.commit()

        book_obj = Book(name = book_name, author_id = author_obj.id)
        db.session.add(book_obj)
        db.session.commit()
    # 有了上面的这一串, 添加表单数据成功, 下面再查询数据库渲染页面, 得到的就是加入数据之后的页面

    '''查询数据库, 渲染模板'''
    authors = Author.query.order_by(Author.id.desc()).all()  # 查询的时候只有filter不用写Author. 其他的都要写来限定是哪一张表
    return render_template("author_book.html", authors=authors, form = form) # 参数:左边的是模板中要用的参数名,右边是这个参数的具体值

@app.route("/delete_book/<int:id>")
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)  # 添加: db.session.add(), 删除: db.session.delete()
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    # 生成数据
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    db.session.add_all([au_xi, au_san, au_qian])
    db.session.commit()

    bk_xi = Book(name='吞噬星空', author_id = au_xi.id)
    bk_xi2 = Book(name='寸芒', author_id = au_xi.id)
    bk_qian = Book(name='飘渺之旅', author_id = au_qian.id)
    bk_san = Book(name='冰火魔厨', author_id = au_san.id)
    db.session.add_all([bk_san, bk_qian, bk_xi2, bk_xi])
    db.session.commit()
    app.run()