from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
import app.config

app = Flask(__name__)
db = SQLAlchemy(app)
migration = Migrate(app,db)
jwt = JWTManager(app)


print(os.environ.get('DEBUG'))
if os.environ.get('DEBUG') == 'true':
    app.config.from_object(config.DevelopmentConfig())
else:
    app.config.from_object(config.ProductionConfig())

from routes import *