from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models import dojo, ninja


@app.route('/ninja/new')
def new_ninja():
    
    return render_template("add_ninja.html", dojos=dojo.Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    print(request.form)
    ninja.Ninja.save(request.form)
    return redirect('/')
