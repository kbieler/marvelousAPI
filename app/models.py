from secrets import token_hex
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin
from uuid import uuid4
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(20))
    
    
   
    def __init__(self, username, email, password, first_name='', last_name= ''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)
        self.api_token = str(token_hex(16))


class M_Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500))
    comics_appear = db.Column(db.String(500))
    super_power = db.Column(db.String(300), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    

    def __init__(self, alias, name, super_power, description='', comics_appear=''):
        self.alias = alias.title()
        self.name = name.title()
        self.description = description
        self.comics_appear = comics_appear
        self.super_power = super_power
        

    def to_dict(self):
        return{
            'id': self.id,
            'alias': self.alias,
            'name': self.name,
            'description': self.description,
            'comics_appear': self.comics_appear,
            'super_power': self.super_power,
            'created': self.created,
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])