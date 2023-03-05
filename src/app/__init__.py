
import os
from flask import Flask, request
from dotenv import load_dotenv
import datetime




from peewee import *

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_SECRET")

if os.getenv('TESTING') == "true":
    print('Running in test mode')
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared',
                          uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )




class TimelinePost(Model):

    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
from app import routes
print(mydb)
