# import Flask class from flask module
from flask import Flask, render_template, jsonify

# create an app (an object of the Flask class)
app = Flask(__name__)

# simulate a job database
JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Montreal, Quebec',
        'salary': '$65,000'
    },
    {
        'id': 2,
        'title': 'Machine Learning Engineer',
        'location': 'Ottawa, Ontario',
        'salary': '$75,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Guelph, Ontario',
        'salary': '$80,000'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Regina, Saskatchewan',
        'salary': '$60,000'
    }
]

# register a route (part of the URL after the main name e.g. www.kgtabiri.com/research)
@app.route("/") # "/" is simply the home or index page
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) # convert JOBS list to json string


if __name__ == '__main__':
    app.run(debug=True)