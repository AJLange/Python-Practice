from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.message import Message
from flask_app.models.user import User
from flask import render_template,redirect,request,session

@app.route('/post_message', methods=['POST'])
def post_mess():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save(data)
    return redirect('/wall')


@app.route('/delete/message/<int:id>')
def del_mes(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/wall')