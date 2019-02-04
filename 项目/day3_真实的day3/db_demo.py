
#coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库，创建数据库链接对象
class MyConfig(object):
    DEBUG = True
    # 连接数据库的信息           协议名
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python02"
    # 让Sqlalchemy跟踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 让Sqlalchemy显示执行的SQL语句
    SQLALCHEMY_ECHO = True

app.config.from_object(MyConfig)
# 创建Sqlalchemy的数据库链接对象: 连接的是app对应的数据库
db = SQLAlchemy(app)

class Role(db.Model): # django中的模型类继承models.Model, flask中的模型类继承数据库连接对象.Model: db.Model

    __tablename__ = "tbl_roles"  # 自定义数据库表名

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # users没有Column并不是字段, 从role出发想看users,仅仅是查询用的而且跟下面的表关联: 用db.relationship：　给role用
    users = db.relationship("User", backref= "role") # backref: 给user用,backref相当于加了一个属性,拿出来的就是一个对象了,上面的id拿出来只是id

    def __repr__(self):
        return "Role: %s" % self.name


class User(db.Model):

    __tablename__ = "tbl_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id")) # 作为另一张表的某个字段的外键

    def __repr__(self):
        return "User: %s" % self.name


if __name__ == '__main__':
    db.drop_all() # 一般不要用
    db.create_all()

    role1 = Role(name="admin") # id自增不用管, users不是字段名
    db.session.add(role1)
    db.session.commit()

    role2 = Role(name="staff")
    db.session.add(role2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role1.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    # 一次保存多条记录
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()