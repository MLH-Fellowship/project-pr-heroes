import datetime

from peewee import *

from app import mydb


class TimelinePost(Model):

    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
