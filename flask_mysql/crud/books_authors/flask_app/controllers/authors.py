from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/create/author', methods=['POST'])
def create_auth():
    Author.save(request.form)
    return redirect('/')

@app.route('/')
def authors():    
    return render_template("authors.html", authors=Author.get_all())

@app.route('/author/<int:id>')
def show_author(id):
    data = {
        'id':id
    } 
    return render_template("author_page.html", author=Author.get_one_with_books(data), unfavorited_books=Book.unfavorited_books(data))

@app.route('/author/addfav', methods=['POST'])
def author_fav():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")
