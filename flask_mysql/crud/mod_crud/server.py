from flask_app import app
from flask import render_template, redirect, request, url_for
# ...server.py

from flask_app.controllers.users import User

@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def users():
    return render_template("index.html", users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("add_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = { 
        "id":id 
        }
    this_user = User.get_one(data)
    return render_template("edit_user.html", user=this_user)


@app.route('/user/show/<int:id>')
def show(id):
    data = { 
        "id":id 
        }
    return render_template("show_user.html", user=User.get_one(data))

@app.route('/user/update/<int:id>',methods=['POST'])
def update(id):
    User.update(request.form)
    
    return redirect(f'/user/show/{id}')


@app.route('/user/delete/<int:id>')
def delete(id):
    data = { 
        "id":id 
        }
    User.destroy(data)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)
