from sqlite3 import Connection as SQLite3Connection
from datetime import datetime

from sqlalchemy import event
from sqlalchemy.engine import Engine

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

import linked_list
import hash_table
import binary_search_tree
from random import shuffle

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


# models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(200))
    posts = db.relationship("BlogPost", cascade="all, delete")


class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


# routes
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        phone=data['phone']
    )
    db.session.add(new_user)
    db.commit()
    return jsonify({"message": "User created"}), 200


@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
    users = User.query.all()
    all_users = linked_list.LinkedList()
    for user in users:
        all_users.insert_beginning(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone
            }
        )
    return jsonify(all_users.to_list()), 200


@app.route('/user/ascending_id', methods=['GET'])
def get_all_user_ascending():
    users = User.query.all()
    all_users = []
    for user in users:
        all_users.append(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone
            }
        )
    return jsonify(all_users), 200


@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    users = User.query.all()
    all_users = linked_list.LinkedList()
    for user in users:
        all_users.insert_beginning(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'phone': user.phone
            }
        )
    return jsonify(all_users.get_user_by_id(user_id)), 200


@app.route('/user/<int:user_id>', methods=['DELETE'])  # TODO: download postman
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify(), 200


@app.route('/blog/<int:user_id>', methods=["POST"])
def create_blog_post(user_id):
    data = request.json
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'message': 'user does not exist'}), 400

    hash_ = hash_table.HashTable(10)
    hash_.add_key_value('title', data['title'])
    hash_.add_key_value('body', data['body'])
    hash_.add_key_value('date', now)
    hash_.add_key_value('user_id', user_id)

    post = BlogPost(
        title=hash_.get_value('title'),
        body=hash_.get_value('body'),
        date=hash_.get_value('date'),
        user_id=hash_.get_value('user_id')
    )
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "new blog post created"}), 200


@app.route('/blog/<int:blog_id>', methods=["GET"])
def get_one_post(blog_id):
    posts = BlogPost.query.all()
    shuffle(posts)

    bst = binary_search_tree.BinarySearchTree()
    for post in posts:
        bst.insert(
            {
                'id': post.id,
                'title': post.title,
                'body': post.body,
                'user_id': post.user_id,
            }
        )
    post = bst.search(blog_id)
    if not post:
        return jsonify({"message": "post not found"})
    return jsonify(post), 200


# @app.route()
# def delete_one_post():
#     pass


if __name__ == '__main__':
    app.run(debug=True)  # TODO: Change the server to *waitress*
