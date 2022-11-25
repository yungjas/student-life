from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from model.Book import Book
from config import db, app

# have to use a different variable name from the file you are trying to blueprint otherwise error will occur 
# see: https://stackoverflow.com/questions/38178776/function-object-has-no-attribute-name-when-registering-blueprint

book_blueprint = Blueprint("book", __name__)


@book_blueprint.route("/api/book/all", methods=["GET"])
def get_books_all():
    book_list = Book.query.all()

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


@book_blueprint.route("/api/book/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.filter_by(book_id=book_id).first()
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


@book_blueprint.route("/api/book/create", methods=["POST"])
def create_book():
    data = request.get_json()
    book = Book(**data)

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


@book_blueprint.route("/api/book/update/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    # retrieve the book to be changed
    book = Book.query.filter_by(book_id=book_id).first()

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


@book_blueprint.route("/api/book/delete/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    # retrieve the book to be deleted
    book = Book.query.filter_by(book_id=book_id).first()

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