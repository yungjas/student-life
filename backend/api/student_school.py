from flask import request, jsonify, Blueprint
from model.StudentSchool import Student, School
from config import db, app
from middleware.middleware import token_required

student_school_blueprint = Blueprint("student_school", __name__)


@student_school_blueprint.route("/api/student/all", methods=["GET"])
@token_required
def get_student_all(current_user):
    student_list = Student.query.all()
    if len(student_list):
        return jsonify(
            {
                "code": 200,
                "data":{
                    "students": [student.json() for student in student_list]
                }
            }
        ),200
    
    return jsonify(
        {
            "code": 404,
            "message": "There are no students"
        }
    )


@student_school_blueprint.route("/api/school/all", methods=["GET"])
@token_required
def get_school_all(current_user):
    school_list = School.query.all()
    if len(school_list):
        return jsonify(
            {
                "code": 200,
                "data":{
                    "schools": [school.json() for school in school_list]
                }
            }
        ),200
    
    return jsonify(
        {
            "code": 404,
            "message": "There are no schools"
        }
    )