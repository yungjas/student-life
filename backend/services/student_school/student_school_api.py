from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

# flask configs
app = Flask(__name__)
db = SQLAlchemy(app)

# CORS config
CORS(app)

# db configs
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+mysqlconnector://root@localhost:3308/student_school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6000, debug=True)
