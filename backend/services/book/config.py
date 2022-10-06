from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

# flask configs
app = Flask(__name__)
db = SQLAlchemy(app)

# CORS config
CORS(app)

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+mysqlconnector://root@localhost:3308/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}