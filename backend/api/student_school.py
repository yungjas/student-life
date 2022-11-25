from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from model.StudentSchool import Student, School
from os import environ
from config import db, app

student_school_blueprint = Blueprint("student_school", __name__)


@student_school_blueprint.route("/api/student/all", methods=["GET"])
def get_student_all():
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
def get_school_all():
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