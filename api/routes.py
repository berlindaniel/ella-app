from flask import Flask, request, jsonify, flash, redirect, url_for
from api import app, db
from api.models import User, UserSchema, Clothing, ClothingSchema, Matches, MatchesSchema
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# Init schema
user_schema = UserSchema()
clothing_schema = ClothingSchema();
match_schema = MatchesSchema();
users_schema = UserSchema(many=True)
clothings_schema = ClothingSchema(many=True);
matches_schema = MatchesSchema(many=True);

@app.route('/')
def index():
    return 'index'

########## USERS ##########

# POST: Create a user
@app.route('/user', methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']

    user = User(username=username, email=email)
    user.set_password(password)
    user.first_name = first_name
    user.last_name = last_name
    user.location = location

    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)

# GET: Get all users
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# GET: Get a user
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# GET: Get current user
@app.route('/currentuser', methods=['GET'])
@login_required
def get_current_user():
    id = current_user.get_id()
    user = User.query.get(id)
    return user_schema.jsonify(user)

# PUT: Update a user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']

    user = User(username=username, email=email)
    user.set_password(password)
    user.first_name = first_name
    user.last_name = last_name
    user.location = location

    db.session.commit()

    return user_schema.jsonify(user)

# DELETE: Delete a user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

# GET/POST: Signup a user
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']

    user = User(username=username, email=email)
    user.set_password(password)
    user.first_name = first_name
    user.last_name = last_name
    user.location = location

    db.session.add(user)
    db.session.commit()

    login_user(user)

    return user_schema.jsonify(user)

# GET/POST: Login a user
@app.route('/signin', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(username=request.json['username']).first()
    if user is None or not user.check_password(request.json['password']):
        flash('Invalid username or password')
        return redirect('/login')
    login_user(user)
    return user_schema.jsonify(user)

# Logout a user
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

########## PROFILE ##########

@app.route('/edit_profile', methods=['PUT'])
@login_required
def edit_profile():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    location = request.json['location']

    user = User(username=username, email=email)
    user.set_password(password)
    user.first_name = first_name
    user.last_name = last_name
    user.location = location

    db.session.commit()
    flash('Your changes have been saved.')

    return redirect(url_for('edit_profile'))

########## CLOTHING ##########

# POST: Create a clothing item
@app.route('/clothing', methods=['POST'])
@login_required
def add_clothing():
    user_id = current_user.get_id()
    name = request.json['name']
    color = request.json['color']
    occasion = request.json['occasion']
    type = request.json['type']

    new_clothing = Clothing(user_id, name, color, occasion, type)

    db.session.add(new_clothing)
    db.session.commit()

    return clothing_schema.jsonify(new_clothing)

# GET: Get all clothing for the logged in user
@app.route('/clothing', methods=['GET'])
@login_required
def get_clothing():
  all_clothing = Clothing.query.filter_by(user_id = current_user.get_id())
  result = clothings_schema.dump(all_clothing)
  return jsonify(result)

# DELETE: Delete a clothing item
@app.route('/clothing/<id>', methods=['DELETE'])
def delete_clothing(id):
    clothing = Clothing.query.get(id)

    db.session.delete(clothing)
    db.session.commit()

    return clothing_schema.jsonify(clothing)

########## MATCHES ##########

# POST: Create a match
@app.route('/matches', methods=['POST'])
@login_required
def add_match():
    user_id = current_user.get_id()
    id1 = request.json['clothing_id1']
    id2 = request.json['clothing_id2']

    new_match = Matches(id1, id2, user_id)

    db.session.add(new_match)
    db.session.commit()

    return match_schema.jsonify(new_match)

# GET: Get all matches
@app.route('/matches', methods=['GET'])
@login_required
def get_matches():
  all_matches = Matches.query.filter_by(user_id = current_user.get_id())
  result = matches_schema.dump(all_matches)
  return jsonify(result)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
