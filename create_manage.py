from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/information')
def information():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('SELECT * FROM employee')
    employees = c.fetchall()
    conn.close()
    return render_template('information.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)

