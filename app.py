from flask import Flask, request
import random
import os
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect('applicants.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS applicants
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  app_num TEXT, name TEXT, email TEXT, phone TEXT, dob TEXT,
                  gender TEXT, marital TEXT, religion TEXT, state TEXT, lga TEXT,
                  country TEXT, id_type TEXT, work TEXT, passport TEXT)''')
    conn.commit()
    conn.close()

init_db()

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

states_lga = {
    "Lagos": ["Ikeja", "Surulere", "Lagos Island", "Lagos Mainland", "Yaba"],
    "Abuja": ["Garki", "Wuse", "Maitama", "Asokoro"],
    "Anambra": ["Onitsha North", "Onitsha South", "Awka South", "Nnewi North"],
    "Rivers": ["Port Harcourt", "Obio-Akpor", "Eleme"]
}

@app.route("/")
def home():
    return """
    <html>
        <head>
            <style>
                body {background-color: #1a1a2e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 50px;}
                h1 { color: #00ff88; font-size: 40px; }
                button {background-color: #00ff88; color: #1a1a2e; border: none; padding: 15px 30px; font-size: 18px; border-radius: 10px; cursor: pointer; margin-top: 10px;}
                a {color: #00ff88; text-decoration: none; font-size: 20px; margin: 0 10px;}
                .form-box {background-color: #0f3460; padding: 20px; border-radius: 15px; width: 70%; margin: 30px auto;}
            </style>
        </head>
        <body>
            <h1>SEN. NATASHA SUPPORTERS NETWORK 🎉</h1>
            <p>Built with Flask + Python</p>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/services">Services</a> | 
            <a href="/portfolio">Portfolio</a> | 
            <a href="/blog">Blog</a> | 
            <a href="/signup">Sign Up</a> | 
            <a href="/contact">Contact</a>
        </body>
    </html>
    """

@app.route('/portfolio')
def portfolio():
    return """
    <html><head><style>
    body {background-color: #1a1a2e; color: #ffffff; font-family: Arial; text-align: center; padding-top: 80px;}
    h1 { color: #00ff88; font-size: 40px; }
    .project {background-color: #0f3460; margin: 20px auto; padding: 20px; border-radius: 15px; width: 70%;}
    a {color: #00ff88; text-decoration: none; font-size: 18px; margin: 15px;}
    </style></head><body>
    <h1>My Portfolio</h1>
    <div class="project"><h2>Project 1: First Flask Website</h2><p>Built with Python + HTML + CSS. That's this site!</p></div>
    <a href="/">Home</a>
    </body></html>
    """

@app.route("/about")
def about():
    return "<html><body style='background:#16213e;color:white;text-align:center;padding-top:100px;'><h1 style='color:#ff00ff;'>About Me</h1><p>This is my first Flask website built!</p><a href='/' style='color:#00ff88;'>← Back to Home</a></body></html>"

@app.route("/services")
def services():
    return "<html><body style='background:#0f3460;color:white;text-align:center;padding-top:100px;'><h1 style='color:#00ff88;'>My Services</h1><p>I build websites with Flask + Python</p><a href='/' style='color:#00ff88;'>← Home</a></body></html>"

@app.route("/contact")
def contact():
    return "<html><body style='background:#16213e;color:white;text-align:center;padding-top:100px;'><h1 style='color:#ff00ff;'>Contact Me</h1><p>Email: youremail@gmail.com</p><a href='/' style='color:#00ff88;'>← Home</a></body></html>"

@app.route("/blog")
def blog():
    return "<html><body style='background:#16213e;color:white;text-align:center;padding-top:80px;'><h1 style='color:#ff00ff;'>My Blog</h1><a href='/' style='color:#00ff88;'>Home</a></body></html>"

@app.route("/testimonials")
def testimonials():
    return "<html><body style='background:#0f3460;color:white;text-align:center;padding-top:80px;'><h1 style='color:#00ff88;'>What People Say</h1><a href='/' style='color:#00ff88;'>Home</a></body></html>"

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    app_num = "APP" + str(random.randint(10000, 99999))
    if request.method == 'POST':
        data = (app_num, request.form['name'], request.form['email'], request.form['phone'], request.form['dob'], request.form['gender'], request.form['marital'], request.form['religion'], request.form['state'], request.form['lga'], request.form['country'], request.form['id_type'], request.form['work'], app_num + ".jpg")
        file = request.files['passport']
        if file: file.save(os.path.join(UPLOAD_FOLDER, app_num + ".jpg"))
        conn = sqlite3.connect('applicants.db'); c = conn.cursor()
        c.execute("INSERT INTO applicants VALUES (NULL,?,?,?,?,?,?)", data)
        conn.commit(); conn.close()
        return f'<script>window.location.href="/profile?app={app_num}"</script>'
    
    state_options = "".join([f'<option value="{s}">{s}</option>' for s in states_lga.keys()])
    return f"<html><body style='background:#1a1a2e;color:white;text-align:center;'><h1>Registration Form</h1><p>App Number: {app_num}</p><form method='POST' enctype='multipart/form-data'><input name='name' placeholder='Name' required><br><input name='email' placeholder='Email' required><br><button>Submit</button></form></body></html>"

@app.route("/profile")
def profile():
    app_num = request.args.get('app', 'APP00000')
    return f"<html><body style='background:#16213e;color:white;text-align:center;padding-top:80px;'><h1>Applicant Dashboard</h1><h2>App: {app_num}</h2><a href='/' style='color:#00ff88;'>Home</a></body></html>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
