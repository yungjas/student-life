import book_model

from config import db, app
from flask import request, jsonify


@app.route("/api/book/all", methods=["GET"])
def get_books_all():
    book_list = book_model.Book.query.all()

    if len(book_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "books": [book.json() for book in book_list]
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no books"
        }
    ), 404


@app.route("/api/book/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = book_model.Book.query.filter_by(book_id=book_id).first()
    if book:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "book": book.json()
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": f"Book with id {book_id} not found"
        }
    ), 404


@app.route("/api/book/create", methods=["POST"])
def create_book():
    data = request.get_json()
    book = book_model.Book(**data)

    try:
        db.session.add(book)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": f"Book was unable to be created due to {e}"
            }
        ), 500
    
    return jsonify(
        {
            "code": 201,
            "data": {
                "book": book.json()
            }
        }
    ), 201


@app.route("/api/book/update/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    # retrieve the book to be changed
    book = book_model.Book.query.filter_by(book_id=book_id).first()

    if book:
        try:
            data = request.get_json()

            if data["book_name"]:
                book.book_name = data["book_name"]
            if data["book_qty"]:
                book.book_qty = data["book_qty"]
            
            # merging new data with existing data
            db.session.merge(book)
            db.session.commit()

            return jsonify(
                {
                    "code": 200,
                    "data":{
                        "book": book.json()
                    }
                }
            ),200
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": f"Book was unable to be updated due to {e}"
                }
            ), 500
    
    return jsonify(
        {
            "code": 404,
            "message": f"Book with id {book_id} not found"
        }
    ), 404


@app.route("/api/book/delete/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    # retrieve the book to be deleted
    book = book_model.Book.query.filter_by(book_id=book_id).first()

    if book:
        try:
            db.session.delete(book)
            db.session.commit()

            return jsonify(
                {
                    "code": 200,
                    "message": "Book deleted"
                }
            ), 200

        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": f"Book was unable to be deleted due to {e}"
                }, 500
            ), 500
    
    return jsonify(
        {
            "code": 404,
            "message": f"Book with id {book_id} not found"
        }
    ), 404 


if __name__ == "__main__":
    # should be binding to 0.0.0.0 if you want the container to be accessible from outside
    app.run(host="0.0.0.0", port=6010, debug=True)
