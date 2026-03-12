from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from dotenv import load_dotenv
import os

load_dotenv()

#database_url = os.getenv('db_url')
secret_key = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key



class CustomerForm(FlaskForm):
    first_name = StringField('first_name', validators=[InputRequired()])
    last_name = StringField('last_name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    phone = StringField('phone', validators=[InputRequired()])
    desc = TextAreaField('desc')

@app.route('/', methods = ['GET', 'POST'])
def home():
    form = CustomerForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone = form.phone.data
        desc = form.desc.data
        return "data submitted"
    return render_template('home.html', form=form)

@app.route('/services-1')
def services():
    return render_template('studio.html')

if __name__ == "__main__":
    app.run(debug=True)