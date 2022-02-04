from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')        
def index():
    if 'counter' in session:
        print('key exists!')
        session['counter'] += 1
    else:
        print("key 'counter' does NOT exist")
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])


@app.route('/destroy_session')        
def clear():
    session.clear()
    return redirect('/')

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

