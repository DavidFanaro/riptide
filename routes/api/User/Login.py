from app import app
from models.User import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


@app.route('/api/v1/login', methods=['POST'])
def login():
    if bool(request.form) is not False:
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        return getUserFromDatabase(username, password)
    elif request.json is not None:
        print(request.json)
        json = request.json
        username = json['username']
        password = json['password']
        return getUserFromDatabase(username, password)
    elif (request.json is None) and (bool(request.form) is False):
        print('no data')
        return 'No data sent', 403
    else:
        print('bad login')
        return 'Bad login', 403


def getUserFromDatabase(username, password):
    user: User = User.query.filter_by(username=username).first()
    if check_password_hash(user.password, password):
        accessToken = create_access_token(identity=username)
        return jsonify(accessToken=accessToken), 200
    else:
        return 'incorrent password', 404
