# import Flask class from flask module
from flask import Flask, render_template

# create an app (an object of the Flask class)
app = Flask(__name__)

# register a route (part of the URL after the main name e.g. www.kgtabiri.com/research)
@app.route("/") # "/" is simply the home or index page
def hello_world():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)