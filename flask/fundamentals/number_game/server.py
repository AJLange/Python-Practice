from flask import Flask, render_template, session, request, redirect
import random 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret key password' # set a secret key for security purposes

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if "randnum" not in session:
        session['randnum'] = random.randint(1,100)
    
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():    
    session['guess'] = int(request.form['guess'])    
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

