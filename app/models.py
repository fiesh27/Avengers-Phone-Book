from app import app, db, login

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from datetime import datetime


@login.user_loader
def load_user(avenger_id):
    return Avenger.query.get(int(avenger_id))

class Avenger(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, unique=False)
    last_name = db.Column(db.String(100), nullable=False, unique=False)
    avenger_name = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, first_name, last_name, avenger_name, address, email, phone_num, password):
        self.first_name = first_name
        self.last_name = last_name
        self.avenger_name = avenger_name
        self.address = address
        self.email = email
        self.phone_num = phone_num
        self.password = self.set_password(password)

    def set_password(self, password):
        pw_hash = generate_password_hash(password)
        return pw_hash

    def __repr__(self):
        return f"<Avenger | {self.name}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('avenger.id'), nullable=False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"<Post | {self.title}>"