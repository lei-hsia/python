# coding: utf-8
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from ihome import create_app, db # 从包名中能直接导入__init__.py中的内容

# 最后除了启动项目的管理工具,其他的数据库,redis,session,csrf都拆到了项目工程目录中

app = create_app("develop")

# 创建管理工具对象
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

@app.route("/")
def index():
    return "index page"

if __name__ == '__main__':
    manager.run()