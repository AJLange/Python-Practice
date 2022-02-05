from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
import random, datetime
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "secretkey here" # set a secret key for security purposes

@app.route('/')        
def index():
    if 'gold' and 'activities' not in session:
        session["gold"] = 0
        session["activities"] = ""
    return render_template('index.html', messages=session["activities"])

@app.route('/process_money' , methods=["POST"])        
def process_gold():
    print(request.form)
    time = datetime.datetime.now()
    location = request.form["building"]
    if location == 'farm':
        gold_this_turn = random.randint(10,20)
    elif location == 'cave':
        gold_this_turn = random.randint(5,10)
    elif location == 'house':
        gold_this_turn = random.randint(2,5)
    elif location == 'casino':
        gold_this_turn = random.randint(-50,50)
    session['gold'] += gold_this_turn
    if gold_this_turn >= 0:
        new_message = f"<p class='greentext'>Yay, you got {gold_this_turn} gold from {location}! ({time})</p>"
        session["activities"] += new_message
    elif gold_this_turn < 0:
        new_message = f"<p class='redtext'>Uh oh, you lost {gold_this_turn} gold at the casino. ({time})</p>"
        session["activities"] += new_message

    return redirect('/')

@app.route('/reset')
def reset_gold():
    session.clear()
    return redirect('/')

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

