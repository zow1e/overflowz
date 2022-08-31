import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from werkzeug.utils import secure_filename

from form import carbonForm
import shelve, user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOAD_FOLDER'] = 'static/images'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/tabs')
def tabs():
   return render_template('tabform.html')

@app.route('/carbonform', methods=['GET', 'POST'])
def create_user():
   createform = carbonForm(request.form)

   return render_template('carbonform.html', form = createform)

@app.route('/dashboard')
def dash():
   return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)