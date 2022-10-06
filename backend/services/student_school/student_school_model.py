from student_school_api import db

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