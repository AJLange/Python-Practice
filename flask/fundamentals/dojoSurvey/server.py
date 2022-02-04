from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')        
def index():
    return render_template('index.html')

@app.route('/process' , methods=["POST"])        
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')        
def result():

    return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

