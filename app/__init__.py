from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from app.config import ProductionConfig, DevelopmentConfig

app = Flask(__name__)

if os.environ.get('DEBUG') == 'true':
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(ProductionConfig())

db = SQLAlchemy(app)
migration = Migrate(app,db)
jwt = JWTManager(app)

from routes import *
from models import *