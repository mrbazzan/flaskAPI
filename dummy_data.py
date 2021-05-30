
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime

from sqlalchemy import event
from sqlalchemy.engine import Engine

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from server import User, BlogPost
from random import randrange
from faker import Faker


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flaskapi.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# enforce foreign keys for sqlite3, it isn't enforced automatically
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(db_api_conn, conn_record):
    if isinstance(db_api_conn, SQLite3Connection):
        cursor = db_api_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()
fake = Faker()


for _ in range(200):
    name = fake.name()
    new_user = User(
        name=name,
        phone=fake.phone_number(),
        email=f"{name.lower().replace(' ', '')}@gmail.com"
    )
    db.session.add(new_user)
    db.session.commit()

for _ in range(200):
    new_post = BlogPost(
        title=fake.paragraph(1),
        body=fake.text(),
        date=fake.date_time(),
        user_id=randrange(1, 200)
    )
    db.session.add(new_post)
    db.session.commit()
