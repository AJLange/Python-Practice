from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import render_template,redirect,request,session


@app.route('/recipes/new')
def new_rec():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("addrecipe.html")

@app.route('/recipe/create', methods=['POST'])
def create_r():
    data = {
        "name": request.form['name'],
        "instructions": request.form['instructions'],
        "time_over": request.form['time_over'],
        "description": request.form['description'],
        "time_over": request.form['time_over'],
        "date_made": request.form['date_made'],
        "user_id": request.form['user_id']
    }
    Recipe.save(data)
    return redirect('/dashboard')


@app.route('/recipes/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show_rec(id):
    data = {
        "id": id
    }
    user_id = {
        "id": session['user_id']
    }
    recipe = Recipe.get_by_id(data)
    print(recipe)
    return render_template("recipe.html", user=User.get_by_id(user_id), recipe=recipe)

@app.route('/recipes/edit/<int:id>')
def edit_rec(id):
    data = {
        "id": id
    }    
    recipe = Recipe.get_by_id(data)
    print(recipe)
    return render_template("editrecipe.html", recipe=recipe)

@app.route('/recipes/update' , methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/dashboard')
    data = {
        "name": request.form['name'],
        "instructions": request.form['instructions'],
        "time_over": request.form['time_over'],
        "description": request.form['description'],
        "time_over": request.form['time_over'],
        "date_made": request.form['date_made'],
        "id": request.form['id']
    }    
    
    Recipe.update(data)
    return redirect('/dashboard')

