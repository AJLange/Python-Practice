from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models import author,book

@app.route('/create/book', methods=['POST'])
def create_book():
    book.Book.save(request.form)
    return redirect('/book/add')

@app.route('/book/add')
def book_add():
    return render_template("books.html", books=book.Book.get_all())

@app.route('/book/<int:id>')
def book_show(id):
    data = {
        'id':id
    } 
    return render_template("book_page.html", book=book.Book.get_by_id(data))

