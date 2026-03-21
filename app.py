from flask import Flask, render_template, url_for, redirect, request
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

secret_key = os.getenv('SECRET_KEY')
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://root:{password}@localhost:{port}/charter"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db.init_app(app)

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    inquiry = db.Column(db.String(20), nullable = False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/studio')
def services():
    return render_template('studio.html')

@app.route('/thankyou')
def thx():
    return render_template('thanks.html')

@app.route('/inquiry', methods = ['POST'])
def inquiry():
    f_first_name = request.form.get('first_name')
    f_last_name = request.form.get('last_name')
    f_email = request.form.get('email')
    f_phone = request.form.get('phone')
    f_inquiry = request.form.get('desc')
    customer = Customers(first_name = f_first_name, last_name=f_last_name, email=f_email, phone=f_phone, inquiry=f_inquiry)
    db.session.add(customer)
    db.session.commit()
    return redirect(url_for('thx'))
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)