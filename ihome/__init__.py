# -*- coding: utf-8 -*-

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# cSrf 防护导入
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config

# 创建flask应用
app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 创建连接mysql对象
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启cSrf保护
CSRFProtect(app)

# 使用session扩展,将session数据存储到redis
Session(app)
