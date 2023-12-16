'''
将Web App所需要的三个表用Model表示出来
'''

import time,uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

#创建唯一标识符
def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

#users表
class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    email = StringField(column_type='varchar(50)')
    passwd = StringField(column_type='varchar(50)')
    admin = BooleanField()
    name = StringField(column_type='varchar(50)')
    image = StringField(column_type='varchar(500)')
    created_at = FloatField(default=time.time)

#blogs表
class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    user_id = StringField(column_type='varchar(50)')
    user_name = StringField(column_type='varchar(50)')
    user_image = StringField(column_type='varchar(500)')
    name = StringField(column_type='varchar(50)')
    summary = StringField(column_type='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

#commments表
class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, column_type='varchar(50)')
    blog_id = StringField(column_type='varchar(50)')
    user_id = StringField(column_type='varchar(50)')
    user_name = StringField(column_type='varchar(50)')
    user_image = StringField(column_type='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)