from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request


@app.route('/')        
def index():
    return render_template('index.html')

@app.route('/process' , methods=["POST"])        
def submit():
    print(request.form)
    if not Dojo.validate_survey(request.form):
        return redirect('/')
    else: #no errors
        Dojo.save(request.form)
    return redirect('/result')

@app.route('/result')        
def result():

    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


