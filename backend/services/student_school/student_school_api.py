import student_school_model

from flask import Flask, request, jsonify
from config import app, db


@app.route("/api/student/all", methods=["GET"])
def get_student_all():
    student_list = student_school_model.Student.query.all()
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


@app.route("/api/school/all", methods=["GET"])
def get_school_all():
    school_list = student_school_model.School.query.all()
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


if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6000, debug=True)
