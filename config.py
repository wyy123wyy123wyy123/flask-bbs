#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

SQLALCHEMY_DATABASE_URI = 'mysql://mysql7748355:L8tjsW5ssN@h46.hmsql.cn/mysql7748355_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True


