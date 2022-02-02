from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def chex():
    return render_template('index.html', num=8, num2=8)

@app.route('/<num>')
def chex_num(num):
    try:
        int(num)
        return render_template('index.html', num=int(num), num2=8)
    except ValueError:
        return "Only an integer value is acceptable here."

@app.route('/<int:num>/<int:num2>')
def chex_num2(num, num2):
    try:
        return render_template('index.html', num=int(num), num2=int(num2))
    except ValueError:
        return "Only an integer value is acceptable here."

@app.route("/<int:num>/<int:num2>/<color1>") 
def chex_color(num, num2, color1):
    try:
        return render_template('index.html', num=int(num), num2=int(num2), color1=color1)  
    except ValueError:
        return "Only an integer value is acceptable here."
    

@app.route("/<int:num>/<int:num2>/<color1>/<color2>") 
def chex_color2(num, num2, color1, color2):
    try:
        return render_template('index.html', num=int(num), num2=int(num2), color1=color1, color2=color2)
    except ValueError:
        return "Only an integer value is acceptable here."

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

