from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def init_db_with_test_users():
    """Создание начальных пользователей."""
    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            users = [
                User(username="User1", balance=5000),
                User(username="User2", balance=7000),
                User(username="User3", balance=9000),
                User(username="User4", balance=11000),
                User(username="User5", balance=15000)
            ]
            db.session.bulk_save_objects(users)
            db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def update_balance(self, amount):
        if self.balance + amount >= 0:
            self.balance += amount
            db.session.commit()
        else:
            raise ValueError("Balance can't be negative")

    @staticmethod
    def delete_user(user_id):
        user_to_delete = User.query.get(user_id)
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
        else:
            raise ValueError("User not found")
