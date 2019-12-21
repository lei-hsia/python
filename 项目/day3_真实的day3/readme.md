请求上下文: request, session对象: 每次接收的客户端的信息不同，得到的结果也不一样
应用上下文: current_app: 不同的人开发的app不同：e.g. flask app的路由信息不同, 但是每个人自己的应用程序总是相同的,
          拿到的总是自己当前的app，app的名字无关，但是总是自己的app     
  request, session属于全局变量，多线程同时操作会有资源竞争的问题，flask有"局部全局变量"的设计，所以有请求上下文的概念

flask扩展程序: import Flask-Script: 使得支持像django一样的脚本命令; 
自定义模版过滤器: 过滤器对应的函数传入的参数就是要过滤的左边的数据
Flask-WTF扩展: 模版中不需要自己写表单的前端信息了, 模版变量替代表单信息; POST访问需要在模版中写 form对象.csrf_token,
               csrf_token的配置需要一开始写好 SECRET_KEY
*** form表单中的字段中的值: form.属性名.data属性: 这样才得到字段名对应的值, 否则得到的是字段信息不是字段中的值
----------------
day3: 
1. 控制语句: {% if %}{% endif %}   {% for samp in samples %}{% endfor %}
2. 宏(macro), 继承(block), 包含(将另一个模版加载到当前模版中: include)都是实现代码重用的功能
3. SQLAlchemy: 独立于任何数据库之外的，提供高层的ORM和底层对原生数据库的支持; 
    i. flask-sqlalchemy: 只完成ORM: 类对象--> SQL的转化
    ii. 把SQL发送给数据库的操作: python3: pymysql: mysql对python的驱动程序:建立连接并来回发送SQL语句
        flask中: pip install flask-mysqldb
    django中用 key-value 的形式配置数据库, flask用类似网址的形式
    
4. 数据库中每一张表对应的模型类，的父类都是数据库连接对象db中的Model属性
   类中属性对应表中字段

5. 往表中添加信息: django: Role().save(); 或者 Roles.objects.create();  
                 flask: role = Role(); db.session.add(role)添加任务, db.session.commit()提交任务
                                    或者db.session.add_all()

6. 最常用过滤器: filter, filter_by; 
   返回信息表示: all(), first()
   查询某一个表中的信息:从表对应的类开始: e.g. Role.query.all()
   其实和SQL的查询关键字类似
   
   练习:  为什么 db_demo.py可以run，但是ipython中from db_demo import * 会有NoModule named "flask_sqlalchemy"的问题？
   
7. 需求: A. 页面图书信息的展示; 
        B. 通过表单能添加author-book对的信息: 创建表单对象, 表单对象的属性得到数据，保存进数据库; 
        C. 删除数据: 定义新的视图: 需要前端传过来的数据看删除哪一本书: GET请求方式把参数放在URL中，或者POST方式放在请求体中，两种都可以
                                                             e.g. GET,参数放在URL中: @app.route("/delete_book/<int:id>")
                                                             
           删除之后让用户看到删除之后的主页: 重定向: 到index页面; 对应的链接用url_for反解析
           删除按钮: 若为POST请求发送的, 在书后面添加<a>标签发送ajax请求; 这里是GET请求直接嵌入<a>标签就行了, 因为默认是GET请求
        *************
        定义新的视图: 因为 @app.route("/", methods=["GET","POST"]) GET请求用于展示页面,POST用于添加数据,逻辑已经满了,
        所以需要新的视图
        url_for("视图函数名", 试图函数参数A=B形式): url_for()传入固定的试图函数, 用不同的route()修饰:创建动态的URL
        *************
        数据最重要: 首先要把表的结构设计出来
   做法: 
   a. 创建数据库，写类对象，数据存进数据库
   b. 试图函数: 查询数据库,渲染模版;   前端:模版对应表格
