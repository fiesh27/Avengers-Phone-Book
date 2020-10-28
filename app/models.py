from app import app, db

from werkzeug.security import generate_password_hash, check_password_hash

class Avenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    avenger_name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(256), nullable=False)


    def __init__(self, name, avenger_name, email, password):
        self.name = name
        self.avenger_name = avenger_name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        pw_hash = generate_password_hash(password)
        return pw_hash

    def __repr__(self):
        return f"<Avenger | {self.name}"
