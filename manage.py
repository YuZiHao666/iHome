# -*- coding: utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import app, db

# 创建脚本管理器对象
manage = Manager(app)

# 让app和db建立关联
Migrate(app, db)
manage.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
