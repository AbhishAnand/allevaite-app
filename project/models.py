from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = db.relationship('Post', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.name}' , ' {self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(100))
    content = db.Column(db.Text)
    owner_id = db.Column(db.Integer,db.ForeignKey('user.id') ,nullable=False)
    