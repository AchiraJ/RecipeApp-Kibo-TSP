from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, app
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    # Hash the password and store in the database
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check if provided password is similar to stored password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.id)

    def get_reset_password_token(self, expires_sec=1800):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return s.dumps(self.id, salt='reset-password-salt')

    @staticmethod
    def verify_reset_password_token(token, expires_sec=1800):
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(
                token, salt='reset-password-salt', max_age=expires_sec)
        except:
            return None
        return User.query.get(user_id)
    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('recipes', lazy=True))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('recipes', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    trending = db.Column(db.Boolean, default=False)
    featured = db.Column(db.Boolean, default=False)

    def __init__(self, name, image, description, ingredients, instructions, category, tags, author_id):
        self.name = name
        self.image = image
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.tags = tags
        self.author_id = author_id

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
