from app import app
from models.User import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token

@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.data
    if data is not None:
        if request.form is not None:
            username = request.form['username']
            password = request.form['password']
            return getUserFromDatabase(username,password)
        elif request.json is not None:
            json = request.json
            username = json['username']
            password = json['password']
            return getUserFromDatabase(username,password)
        else:
            return 'Bad login', 403
    else:
        return 'Bad login request', 403

def getUserFromDatabase(username, password):
    user:User = User.query.filter_by(username=username).first()
    if user.password == password:
        accessToken = create_access_token(username=username)
        return jsonify(accessToken=accessToken), 200
    else:
        return 'incorrent password', 404
