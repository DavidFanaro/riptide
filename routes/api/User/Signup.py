from app import app, db
from models.User import User
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from email_validator import validate_email, EmailNotValidError

@app.route('/api/v1/signup', methods=['POST'])
def signUp():
    data = request.data
    if data is not None:
        if bool(request.form) is not False:
            
            return 
        elif request.json is not None:
            json = request.json
            email = json['email']
            firstname = json['firstname']
            lastname = json['lastname']
            username = json['username']
            password = json['password']
            return createUserWithInfo(username,email,password,firstname,lastname)
        elif (request.json is None) and (bool(request.form) is False):
            print('no data')
            return 'No data sent', 403
        else:
            return 'Bad signup', 403
        
    else:
        return 'Bad signup request', 403

def createUserWithInfo(username, email, password, firstname, lastname):
    if checkEmailIsValid(email):
        if len(username) >= 5:
            if len(password) >= 8:
                hashpw = generate_password_hash(password,'sha256')
                newUser = User(username,email,firstname,lastname,hashpw)
                db.session.add(newUser)
                db.session.commit()
                return f'User: {newUser.firstname} {newUser.lastname} Created'
            else:
                return 'Password is too short!! Must be 8 or more characters'
        else:
            return 'Username is too short', 403    
    else:
        return 'Bad Email', 403
    pass

def checkEmailIsValid(email):
    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError  as e:
        return False