from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import render_template,redirect,request

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojo.html", dojos=Dojo.get_all())


@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def view_dojo(id):
    print(request.form)
    data = { 
        "id":id 
        }
    return render_template("show_dojo.html", dojo=Dojo.get_one(data))