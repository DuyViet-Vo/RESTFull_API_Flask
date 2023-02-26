from flask import Blueprint

books = Blueprint("books", __name__)
@books.route('/books_all')
def books_all():
    return "all books"