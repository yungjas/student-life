from config import app 
from api import book, student_school, auth

import os

app.register_blueprint(book.book_blueprint)
app.register_blueprint(student_school.student_school_blueprint)
app.register_blueprint(auth.auth_blueprint)


if __name__ == "__main__":
    # environ variables will be either getting from docker environment is running on docker or from the .env file if running locally
    print(os.environ.get('SQLALCHEMY_DATABASE_URI'))
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6010, debug=True)