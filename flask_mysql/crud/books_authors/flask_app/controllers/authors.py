from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models.author import Author

@app.route('/create/author', methods=['POST'])
def create_auth():
    Author.save(request.form)
    return redirect('/')

@app.route('/')
def authors():    
    render_template("authors.html", authors=Author.get_all())

@app.route('/author/<int:id>')
def show_author(id):    
    render_template("author_info.html", authors=Author.get_one_with_books(id))
