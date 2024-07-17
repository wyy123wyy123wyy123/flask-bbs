from exts import db
from datetime import datetime
from enum import Enum

class PermissionEnum(Enum):
    BOARD = '模块'
    POST = '帖子'
    COMMENT = '评论'
    FRONT_USER = '前台用户'
    CMS_USER = '后台用户'

class PermissionModel(db.Model):
    __tablename__ = "permission"
    id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    name = db.Column(db.Enum(PermissionEnum),nullable = False,unique=True)