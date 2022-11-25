from config import app 
from api import book, student_school

import os

app.register_blueprint(book.book_blueprint)
app.register_blueprint(student_school.student_school_blueprint)


if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    print(os.environ.get('SQLALCHEMY_DATABASE_URI'))
    app.run(host="0.0.0.0", port=6010, debug=True)