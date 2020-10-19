from flask import Flask, request, jsonify
from api import app, db
from api.models import User, UserSchema

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# POST: Create a user
@app.route('/user', methods=['POST'])
def add_user():
  username = request.json['username']
  password = request.json['password']
  first_name = request.json['first_name']
  last_name = request.json['last_name']
  location = request.json['location']

  new_user = User(username, password, first_name, last_name, location)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

# GET: Get all users
@app.route('/user', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result)

# GET: Get single user
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  return user_schema.jsonify(user)

# PUT: Update a user
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
  user = User.query.get(id)

  username = request.json['username']
  password = request.json['password']
  first_name = request.json['first_name']
  last_name = request.json['last_name']
  location = request.json['location']

  user.username = username
  user.password = password
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

# Run Server
if __name__ == '__main__':
  app.run(debug=True)