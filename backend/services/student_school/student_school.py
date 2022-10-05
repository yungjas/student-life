from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

# flask configs
app = Flask(__name__)
db = SQLAlchemy(app)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql+mysqlconnector://root@localhost:3308/student_school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


class School(db.Model):
    __tablename__ = 'school'
    school_id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(64), nullable=False)

    def __init__(self, school_id, school_name):
        self.school_id = school_id
        self.school_name = school_name
        
    def json(self):
        return {
            "school_id": self.school_id,
            "school_name": self.school_name,
        }

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(64), nullable=False)
    school_id = db.Column(db.ForeignKey('school.school_id'), nullable=False, index=True)

    def __init__(self, student_id, student_name, school_id):
        self.student_id = student_id
        self.student_name = student_name
        self.school_id = school_id

    school = db.relationship("School", primaryjoin="Student.school_id == School.school_id", backref="student")
    
    def json(self):
        return {
            "student_id": self.student_id,
            "student_name": self.student_name,
            "school_id": self.school_id
        }

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6000, debug=True)
