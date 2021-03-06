from api import db, ma, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class/model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    location = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location
        }

        return data

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    color = db.Column(db.String(100))
    occasion = db.Column(db.String(100))
    type = db.Column(db.String(100))

    def __init__(self, user_id, name, color, occasion, type):
        self.user_id = user_id
        self.name = name
        self.color = color
        self.occasion = occasion
        self.type = type

class Outfit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    top_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))
    bottom_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))
    shoes_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))

    def __init__(self, user_id, top_id, bottom_id, shoes_id):
        self.user_id = user_id
        self.top_id = top_id
        self.bottom_id = bottom_id
        self.shoes_id = shoes_id

class Favorite(db.Model):
    outfit_id = db.Column(db.Integer, db.ForeignKey('outfit.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(100))
    description = db.Column(db.String(400))
    rating = db.Column(db.Integer)

    def __init__(self, outfit_id, user_id, name, description, rating):
        self.outfit_id = outfit_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.rating = rating

class Matches(db.Model):
    clothing_id1 = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)
    clothing_id2 = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, clothing_id1, clothing_id2, user_id):
        self.clothing_id1 = clothing_id1
        self.clothing_id2 = clothing_id2
        self.user_id = user_id

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    clothing_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))
    clothing_name = db.Column(db.String(100))
    impression = db.Column(db.String(100))
    stars = db.Column(db.Integer)
    text = db.Column(db.String(400))

    def __init__(self, user_id, clothing_id, clothing_name, impression, stars, text):
        self.user_id = user_id
        self.clothing_id = clothing_id
        self.clothing_name = clothing_name
        self.impression = impression
        self.stars = stars
        self.text = text

class Belongs(db.Model):
    clothing_id = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'location')

class OutfitSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'top_id', 'bottom_id', 'shoes_id')

class FavoriteSchema(ma.Schema):
    class Meta:
        fields = ('outfit_id', 'user_id', 'name', 'description', 'rating')

class ClothingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'name', 'color', 'occasion', 'type')

class MatchesSchema(ma.Schema):
    class Meta:
        fields = ('clothing_id1', 'clothing_id2', 'user_id')

class ReviewSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'clothing_id', 'clothing_name', 'impression', 'stars', 'text')

class BelongsSchema(ma.Schema):
    class Meta:
        fields = ('clothing_id', 'user_id')
