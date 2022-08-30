import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from werkzeug.utils import secure_filename



app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOAD_FOLDER'] = 'static/images'


@app.route('/')
def home():
   return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)