from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hi " + str(name)

@app.route('/repeat/<count>/<word>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def repeat(count, word):   

        
    fullstring = "" 
    try:
        int(count)
        for i in range(0, int(count)):
            fullstring = fullstring + str(word) + " "
        return fullstring
    except ValueError:
        return "Please enter an integer for repeating."

@app.errorhandler(404) 
def not_found(e):
    return "Sorry! No response! Try again!"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

