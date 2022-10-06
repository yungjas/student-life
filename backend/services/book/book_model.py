from config import db

class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(64), nullable=False)
    book_qty = db.Column(db.Integer, nullable=False)

    def __init__(self, book_name, book_qty):
        self.book_name = book_name
        self.book_qty = book_qty
        
    def json(self):
        return {
            "book_id": self.book_id,
            "book_name": self.book_name,
            "book_qty": self.book_qty
        }