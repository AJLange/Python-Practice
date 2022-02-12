from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models import author,book

@app.route('/create/book', methods=['POST'])
def create_book():
    book.Book.save(request.form)
    return redirect('/books')


