# if you put Flask and db configs under app.py, since in this scenario api files import Flask and db configs from app.py also, when app.py tries to import api files for Blueprint, it will cause a circular import error

# hence best is to have a separate config file so that files in models and api as well as app.py can import Flask and db configs from here
# then if app.py wants to import api files for Blueprint, will not have circular import error

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

import os

# flask configs
app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# CORS config
CORS(app)

# db config
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

