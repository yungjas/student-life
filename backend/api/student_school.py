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

@student_school_blueprint.route("/api/student/create", methods=["POST"])
@token_required
def create_student(current_user):
    data = request.get_json()
    student = Student(**data)
    try:
        db.session.add(student)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": f"Student was unable to be created due to {e}"
            }
        ), 500
    return jsonify(
            {
                "code": 201,
                "message": "Student was created"
            }
        ), 201

@student_school_blueprint.route("/api/school/create", methods=["POST"])
@token_required
def create_school(current_user):
    data = request.get_json()
    school = School(**data)
    try:
        db.session.add(school)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": f"School was unable to be created due to {e}"
            }
        ), 500
    return jsonify(
            {
                "code": 201,
                "message": "School was created"
            }
        ), 201

@student_school_blueprint.route("/api/school/update/<int:school_id>", methods=["PUT"])
@token_required
def update_school(current_user, school_id):
    school = School.query.filter_by(school_id=school_id).first()
    if school:
        try:
            data = request.get_json()
            if data["school_name"]:
                school.school_name = data["school_name"]
                db.session.merge(school)
                db.session.commit()

                return jsonify(
                    {
                        "code": 200,
                        "data":{
                            "book": school.json()
                        }
                    }
                ), 200
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": f"School was unable to be updated due to {e}"
                }
            ), 500