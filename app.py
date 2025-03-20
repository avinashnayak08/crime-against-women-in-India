from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import sqlite3

# Path to the SQLite database
DATABASE = 'database/data1.db'


def connect_db():
    """Connect to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Optional: Access rows as dictionaries
    return conn
@app.route('/')
def home():
    return render_template('home.html', page="Home")


@app.route('/about')
def about():
    return render_template('about.html', page="About")


@app.route('/application')
def application():
    return render_template('application.html', page="Application")


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        state = request.form.get('state')
        # Query logic or fetch data for the selected state
        data = []  # Replace with actual query results
        return render_template('info.html', content=data, state=state)
    return render_template('search.html', page="Search")


@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        Aadhaar_Number = request.form['Aadhaar_Number']
        Type_of_Crime = request.form['Type_of_Crime']
        State = request.form['State']
        City = request.form['City']
        Date_of_Incident = request.form['Date_of_Incident']
        Description = request.form['Description']

        # Example: Logging the complaint data to the console
        print(
            f"Complaint Filed:\nAadhaar_Number: {Aadhaar_Number}\nType_of_Crime: {Type_of_Crime}\nState: {State}\nCity: {City}\nDate_of_Incident: {Date_of_Incident}\nDescription: {Description}")


        # Redirect to thank you page
        return redirect(url_for('thank_you'))

    return render_template('report.html', page="Report")





@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html', page="Thank You")


if __name__ == '__main__':
    app.run(debug=True)